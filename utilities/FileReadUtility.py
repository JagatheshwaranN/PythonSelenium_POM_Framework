"""
Name : FileReadUtility.py
Author : Jaga
Date : 21-02-2021
"""

import configparser

config = configparser.RawConfigParser()
config.read(".//configuration//Config.ini")


class ReadConfig:
    @staticmethod
    def get_application_url():
        url = config.get('common information', 'BASE_URL')
        return url

    @staticmethod
    def get_username():
        user = config.get('common information', 'USERNAME')
        return user

    @staticmethod
    def get_password():
        password = config.get('common information', 'PASSWORD')
        return password

    @staticmethod
    def get_test_data(test_data):
        data = config.get('common information', test_data)
        return data
