from pathlib import Path

from src.run_agent import load_config


def test_public_config_exists() -> None:
    config_path = Path("config/default.toml")
    assert config_path.exists()


def test_public_config_loads() -> None:
    config = load_config(Path("config/default.toml"))
    assert config["agent_id"] == "public-skeleton"
    assert config["runtime"]["memory_mode"] == "ephemeral"
