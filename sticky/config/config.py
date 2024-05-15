import configparser

config = configparser.ConfigParser()
config.read("./config/config.conf")


class Main:
    DB_name = config["main"]["db_name"]


class Note:
    DB_name = config["note"]["db_name"]


class Macro:
    DB_name = config["macro"]["db_name"]
