import os

def pytest_configure(config):
    from pathlib import Path
    pp = Path(__file__).absolute().parent.parent / 'decks/local-infra-ring/rclone.conf.host-ext-net.conf.toml'
    os.environ['RCLONE_CONFIG_FILE__HOST_EXT'] = str(pp)
    return config

def pytest_unconfigure(config):
    os.environ['RCLONE_CONFIG_FILE__HOST_EXT'] = ''
    return config