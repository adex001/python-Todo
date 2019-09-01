"""Application configuration."""

class Config(object):
    """Base config class."""


class TestingConfig(Config):
    """Configuration for testing environment."""

    DEBUG = True


class DevelopmentConfig(Config):
    """Configuration for development environment."""

    DEBUG = False

config = {
    "testing": TestingConfig,
    "development": DevelopmentConfig
}
