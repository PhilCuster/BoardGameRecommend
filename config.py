import os


class Base():
    BOARDGAME_API_URI = 'https://www.boardgamegeek.com/xmlapi2/'
    ENV = 'production'
    DEBUG = False


class LocalDevelopment():
    BOARDGAME_API_URI = 'https://www.boardgamegeek.com/xmlapi2/'
    ENV = 'development'
    DEBUG = True
