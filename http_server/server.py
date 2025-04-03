from http.server import ThreadingHTTPServer
from http_server.impl.MyRequestHandler import MyRequestHandler


def run(server_class=ThreadingHTTPServer, handler_class=MyRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Serving on port 8000...")
    httpd.serve_forever()


run()