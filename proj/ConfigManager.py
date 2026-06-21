import os
import json
import configparser

Config = configparser.ConfigParser()

_path = os.path.dirname(os.path.realpath(__file__))
config_file_name = "config.json"


def getattr(name):
    json.load()
