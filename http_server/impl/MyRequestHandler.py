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
