class DevelopmentConfig():
    DEBUG=True
    MYSQL_HOST='localhost'
    MYSQL_USER='Karla'
    MYSQL_PASSWORD='4682'
    MYSQL_DB='api_utl'
    MYSQL_CURSORCLASS = 'Cursor'

config={
    'development':DevelopmentConfig
}