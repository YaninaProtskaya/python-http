from http_server.base.BaseHttpServer import BaseHttpServer
from http_server.base.config.Config import Config
from http_server.impl.MyRequestHandler import MyRequestHandler

def run():
    config = Config()
    server = BaseHttpServer(config, MyRequestHandler)
    server.start()

run()
