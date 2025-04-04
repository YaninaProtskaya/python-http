import os
import sys
import yaml

from http_server.base.config.ServerConfig import ServerConfig


class Config:
    @property
    def server(self) -> ServerConfig:
        return self.__server
    @property
    def jsonDir(self) -> str:
        return self.__jsonDir

    @staticmethod
    def __readConfFile():
        try:
            configFilePath = sys.argv[sys.argv.index('-c') + 1]
        except Exception:
            print('Configuration file not specified. Example: -c path/to/file')
            exit(1)

        if os.path.exists(configFilePath):
            with open(configFilePath) as stream:
                try:
                    res = yaml.safe_load(stream)
                    return res
                except yaml.YAMLError as exc:
                    print(exc)
                    exit(1)
        else:
            print('Configuration file does not exist: ' + configFilePath)
            exit(1)

    def __init__(self):
        conf = self.__readConfFile()
        self.__server = ServerConfig(conf['server']['host'], conf['server']['port'])
        self.__jsonDir = conf['json_dir']

    def __str__(self):
        return str({
            'server': self.__server,
            'json_dir': self.__jsonDir
        })

    def __repr__(self):
        return self.__str__()
