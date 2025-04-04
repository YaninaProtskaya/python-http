from http.server import ThreadingHTTPServer

from http_server.base.config.Config import Config


class BaseHttpServer:
    def __init__(self, config: Config, request_handler):
        self.__config = config
        self.__requestHandler = request_handler

    def start(self):
        config = self.__config
        httpd = ThreadingHTTPServer((config.server.host, config.server.port), self.__requestHandler)
        httpd.jsonDir = config.jsonDir # workaround for passing jsonDir to the request handler
        print(f"Listening on http://{config.server.host}:{config.server.port}")
        httpd.serve_forever()


