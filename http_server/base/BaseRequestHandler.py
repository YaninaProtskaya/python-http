from http.server import BaseHTTPRequestHandler
import json

class BaseRequestHandler(BaseHTTPRequestHandler):
    def respond(self, data: str, code: int = 200):
        self.send_response(code)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(str.encode(data))

    def respondJson(self, data: dict[str, any], code: int = 200):
        self.send_response(code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(str.encode(json.dumps(data)))

    def do_GET(self):
        self.handleGet()

    def handleGet(self):
        match self.path:
            case '/':
                self.respond('Hello, Python server!')
            case _:
                self.respond('Not found', 404)




if __name__ == '__main__':
    pass
