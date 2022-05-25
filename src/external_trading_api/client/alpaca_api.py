import configparser
import alpaca_trade_api as tradeapi

class AlpacaAPI(object):

    CONFIG_STORAGE = "config.ini"
    CONFIG_SECTION = "alpaca-read"

    API_KEY = "key"
    API_SECRET = "secret"
    API_URL = "url"

    def get_set_api_by_section(self, section):

        config = configparser.ConfigParser()
        config.read(self.CONFIG_STORAGE)

        self.api = tradeapi.REST(
            config[section][self.API_KEY]
            , config[section][self.API_SECRET]
            , config[section][self.API_URL]
            , 'v2'
        )

        return self.api

    def get_set_api(self):
        return self.get_set_api_by_section(self.CONFIG_SECTION)

    def get_api(self):
        return self.api
