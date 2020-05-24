import configparser

config = configparser.ConfigParser()
config.read('config.ini')
print(config['secrets']['db_password'])
print(type(config['secrets']['db_password']))
print(config['secrets']['django_secret_key'])
print(type(config['secrets']['django_secret_key']))
print(config['server_settings'].getboolean('debug'))
print(type(config['server_settings'].getboolean('debug')))

