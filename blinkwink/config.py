import os

class Config:
    SECRET_KEY = "^\xa1\x93|\xfa\xc0)\xa0R'\x9a9\x1e\xa2\xbe\xdb\r\x1c8\xe4\x05\xa3z\x03"
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False

config_by_name = dict(
                  dev = DevelopmentConfig,
                  test = TestConfig,
                  prod = ProductionConfig
                 )
