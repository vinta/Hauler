# coding: utf-8

import os


class Config(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(Config):
    SENTRY_DSN = os.environ['SENTRY_DSN']


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
