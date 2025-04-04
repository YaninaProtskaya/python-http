from http.server import ThreadingHTTPServer

from http_server.base.config.Config import Config
from http_server.impl.MyRequestHandler import MyRequestHandler

def run():
    config = Config()
    httpd = ThreadingHTTPServer((config.server.host, config.server.port), MyRequestHandler)
    httpd.jsonDir = config.jsonDir # workaround for passing jsonDir to MyRequestHandler
    print(f"Listening on http://{config.server.host}:{config.server.port}")
    httpd.serve_forever()

run()
