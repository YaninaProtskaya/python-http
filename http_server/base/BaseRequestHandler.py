from http.server import BaseHTTPRequestHandler
import json

class BaseRequestHandler(BaseHTTPRequestHandler):
    def sendText(self, data: str, code: int = 200):
        self.send_response(code)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(str.encode(data))

    def sendJson(self, data: dict[str, any], code: int = 200):
        self.send_response(code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(str.encode(json.dumps(data)))

    def do_GET(self):
        self.handleGet()

    def handleGet(self):
        match self.path:
            case '/':
                self.sendText('Hello, Python server!')
            case _:
                self.sendText('Not found', 404)

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        try:
            data = json.loads(post_data)
            self.handlePost(data)
        except json.JSONDecodeError:
            response = {'error': 'Invalid JSON'}
            self.sendJson(response, 400)

    def handlePost(self, data):
        print(f"self.path: ${self.path}")
        match self.path:
            case '/echo' | '/echo/':
                self.sendJson(data)
            case _:
                self.sendJson({'error': 'Not found'}, 404)

    def do_DELETE(self):
        self.handleDelete()

    def handleDelete(self):
        match self.path:
            case '/delete-test':
                response = {'message': 'Resource deleted successfully'}
                self.sendJson(response)
            case _:
                self.sendJson({'error': 'Resource not found'}, 404)


if __name__ == '__main__':
    pass
