import pytest

from aw_client import ActivityWatchClient
from aw_core.config import load_config_toml

default_config = """
[server]
hostname = "127.0.0.1"
port = "5600"

[client]
commit_interval = 10

[server-testing]
hostname = "127.0.0.1"
port = "5666"

[client-testing]
commit_interval = 5
""".strip()


def load_config():
    return load_config_toml("aw-client", default_config)


def test_config_parsing():
    config = load_config()

    # Example assertions
    if isinstance(config["server"]["hostname"], list):
        assert config["server"]["hostname"][0] == "127.0.0.1"
    else:
        assert config["server"]["hostname"] == "127.0.0.1"
    assert config["server"]["port"] == "5600"
    assert config["client"]["commit_interval"] == 10
    assert config["server-testing"]["port"] == "5666"
    assert config["client-testing"]["commit_interval"] == 5
