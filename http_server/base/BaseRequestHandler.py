from http.server import BaseHTTPRequestHandler
import json
import os

from http_server.base.model.HttpMethod import HttpMethod
from http_server.base.model.Request import Request


class BaseRequestHandler(BaseHTTPRequestHandler):
    @property
    def requestData(self) -> Request:
        return self.__requestData

    def __init__(self, request, client_address, server):
        self.__requestData = None
        super().__init__(request, client_address, server)

    def sendText(self, data: str, code: int = 200):
        self.send_response(code)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(str.encode(data))

    def sendError(self, error: str, code: int = 500):
        self.sendJson({'error': error}, code)

    def notFound(self):
        self.sendJson({'error': 'Not found'}, 404)

    def sendJson(self, data: dict[str, any], code: int = 200):
        self.send_response(code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(str.encode(json.dumps(data)))

    def sendJsonFromFile(self, file_path: str):
        jsonDir = self.server.jsonDir # todo pass the configuration
        path = (jsonDir if jsonDir.endswith('/') else jsonDir + '/') + file_path
        if os.path.exists(path):
            f = open(path, 'r')
            fileContents = f.read()
            f.close()
            try:
                res = json.loads(fileContents)
                self.sendJson(res)
            except json.JSONDecodeError:
                self.sendError('Invalid json file')
        else:
            self.sendError(f"File not found '{path}'")

    def do_GET(self):
        self.__requestData = Request(self.path, HttpMethod.GET)
        self.handleGet()

    def handleGet(self):
        match self.path:
            case '/':
                self.sendText('Hello, Python server!')
            case '/info' | '/info/':
                self.sendText('Made by Yanina Protskaya (:')
            case '/file-test':
                self.sendJsonFromFile('test.json')
            case _:
                self.notFound()

    def do_POST(self):
        self.__requestData = Request(self.path, HttpMethod.POST)
        data = self.__readJson()
        self.handlePost(data)

    def handlePost(self, data):
        match self.path:
            case '/echo' | '/echo/':
                self.sendJson(data)
            case _:
                self.notFound()

    def __readJson(self):
        content_length = int(self.headers.get('Content-Length', 0))
        put_data = self.rfile.read(content_length)
        try:
            data = json.loads(put_data)
            return data
        except json.JSONDecodeError:
            self.sendError('Invalid JSON', 400)

    def do_PUT(self):
        self.__requestData = Request(self.path, HttpMethod.PUT)
        data = self.__readJson()
        self.handlePut(data)

    def handlePut(self, data):
        if self.path == '/update-test':
            response = {'message': 'Resource updated successfully', 'updated_data': data}
            self.sendJson(response)
        else:
            self.notFound()

    def do_DELETE(self):
        self.__requestData = Request(self.path, HttpMethod.DELETE)
        self.handleDelete()

    def handleDelete(self):
        match self.path:
            case '/delete-test':
                response = {'message': 'Resource deleted successfully'}
                self.sendJson(response)
            case _:
                self.notFound()
