from http_server.base.BaseRequestHandler import BaseRequestHandler


class MyRequestHandler(BaseRequestHandler):
    def handleGet(self):
        match self.path:
            case '/':
                data = {
                    'message': 'Hello, Python server!'
                }
                self.sendJson(data)

            case '/info' | '/info/':
                self.sendText('Made by Yanina Protskaya (:')

            case _:
                self.sendText('Not found', 404)


    def handlePost(self, data):
        match self.path:
            case '/':
                response = {'message': 'Received!', 'data': data}
                self.sendJson(response)
            case _:
                self.sendJson({'error': 'Not found'}, 404)


    def handlePut(self, data):
        match self.path:
            case '/test/123':
                response = {'message': 'Resource 123 updated successfully', 'updated_data': data}
                self.sendJson(response)
            case '/test/12345':
                response = {'message': 'Resource 12345 updated successfully', 'updated_data': data}
                self.sendJson(response)
            case _:
                self.sendJson({'error': 'Resource not found'}, 404)


    def handleDelete(self):
        match self.path:
            case '/test/123':
                response = {'message': 'Resource 123 deleted successfully'}
                self.sendJson(response)
            case '/test/12345':
                response = {'message': 'Resource 12345 deleted successfully'}
                self.sendJson(response)
            case _:
                self.sendJson({'error': 'Resource not found'}, 404)
