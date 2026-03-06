from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover
    import tomli as tomllib  # type: ignore


def load_config(path: Path) -> dict:
    with path.open("rb") as handle:
        return tomllib.load(handle)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="HomoErectus public runtime skeleton")
    parser.add_argument("--config", default="config/default.toml", help="Path to TOML config")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    config_path = Path(args.config)
    if not config_path.exists():
        print(f"Config not found: {config_path}", file=sys.stderr)
        return 1

    config = load_config(config_path)
    agent_id = config.get("agent_id", "unknown-agent")
    mode = config.get("mode", "bootstrap_restricted")
    runtime = config.get("runtime", {})

    print("HomoErectus public skeleton")
    print(f"agent_id={agent_id}")
    print(f"mode={mode}")
    print(f"event_bus={runtime.get('event_bus', 'unknown')}")
    print(f"memory_mode={runtime.get('memory_mode', 'unknown')}")
    print("status=ready")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
