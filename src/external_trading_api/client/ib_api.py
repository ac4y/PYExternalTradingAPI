import configparser
from ib_insync import *

class InteractiveBrokersAPI(object):

    CONFIG_STORAGE = "config.ini"
    CONFIG_SECTION = "interactive-brokers-ohlc"

    HOST = "host"
    PORT = "port"
    CLIENT_ID = "client-id"

    def get_set_api_by_section(self, section):

        config = configparser.ConfigParser()
        config.read(self.CONFIG_STORAGE)

        self.api = IB()

        self.api.connect(
            config[section][self.HOST]
            , config[section][self.PORT]
            , clientId=config[section][self.CLIENT_ID]
        )

        return self.api

    def get_set_api(self):
        return self.get_set_api_by_section(self.CONFIG_SECTION)

    def get_api(self):
        return self.api
