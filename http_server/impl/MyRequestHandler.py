from http_server.base.BaseRequestHandler import BaseRequestHandler

class MyRequestHandler(BaseRequestHandler):
    def handleGet(self):
        print(self.requestData)
        match self.requestData.path[0]: # todo check index range
            case '/':
                data = {'message': 'Hello, Python server!'}
                self.sendJson(data)

            case 'file-test':
                match self.requestData.path[1]:
                    case '1':
                        self.sendJsonFromFile('test1.json')
                    case '2':
                        self.sendJsonFromFile('test2.json')
                    case _: self.notFound()

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


if __name__ == '__main__':
    pass