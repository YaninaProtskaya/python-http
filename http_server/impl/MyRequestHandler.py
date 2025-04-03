from http_server.base.BaseRequestHandler import BaseRequestHandler


class MyRequestHandler(BaseRequestHandler):
    def handleGet(self):
        match self.path:
            case '/':
                data = {
                    'message': 'Hello, Python server!'
                }
                self.respondJson(data)

            case '/info' | '/info/':
                self.respond('Made by Yanina Protskaya (:')

            case _:
                self.respond('Not found', 404)
