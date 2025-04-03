from http_server.base.BaseRequestHandler import BaseRequestHandler

class MyRequestHandler(BaseRequestHandler):
    JSON_DIR = '/Users/yanina/programming/python/python-http/http_server/json/'

    def sendJsonFromFile(self, file_path: str):
        super().sendJsonFromFile((self.JSON_DIR if self.JSON_DIR.endswith('/') else self.JSON_DIR + '/') + file_path)

    def handleGet(self):
        match self.path:
            case '/':
                data = {'message': 'Hello, Python server!'}
                self.sendJson(data)
            case '/file-test':
                self.sendJsonFromFile('test.json')

            case _: self.notFound()


    def handlePost(self, data):
        match self.path:
            case '/':
                response = {'message': 'Received!', 'data': data}
                self.sendJson(response)

            case _: self.notFound()


    def handlePut(self, data):
        match self.path:
            case '/test/123':
                response = {'message': 'Resource 123 updated successfully', 'updated_data': data}
                self.sendJson(response)
            case '/test/12345':
                response = {'message': 'Resource 12345 updated successfully', 'updated_data': data}
                self.sendJson(response)

            case _: self.notFound()


    def handleDelete(self):
        match self.path:
            case '/test/123':
                response = {'message': 'Resource 123 deleted successfully'}
                self.sendJson(response)
            case '/test/12345':
                response = {'message': 'Resource 12345 deleted successfully'}
                self.sendJson(response)

            case _: self.notFound()
