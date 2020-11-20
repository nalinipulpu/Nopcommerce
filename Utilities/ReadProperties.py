import configparser

conf = configparser.RawConfigParser()
conf.read('.\\Configurations\\Conf.ini')


class ReadConf:
    @staticmethod
    def get_BaseUrl():
        return conf.get('common info', 'BaseUrl')

    @staticmethod
    def get_UserId():
        return conf.get('common info', 'UserId')

    @staticmethod
    def get_Password():
        return conf.get('common info', 'Password')
