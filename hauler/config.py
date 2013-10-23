# coding: utf-8

import os


class Config(object):
    DEBUG = False
    TESTING = False
    LOGGER_NAME = 'hauler'


class ProductionConfig(Config):
    SENTRY_DSN = os.environ.get('SENTRY_DSN', None)


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
