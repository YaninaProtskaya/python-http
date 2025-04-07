from http_server.base.BaseRequestHandler import BaseRequestHandler

class MyRequestHandler(BaseRequestHandler):
    def handleGet(self):
        match self.requestData.path.get(0):
            case '/':
                data = {'message': 'Hello, Python server!'}
                self.sendJson(data)

            case 'goal-file-available-statuses':
                match self.requestData.path.get(1):
                    case '77742':
                        self.sendJsonFromFile('goalfiles/goal-file-available-statuses-77742.json')
                    case '77746':
                        self.sendJsonFromFile('goalfiles/goal-file-available-statuses-77746.json')

                    case _: self.notFound()

            case 'goalfile':
                match self.requestData.path.get(1):
                    case '77742':
                        self.sendJsonFromFile('goalfiles/77742.json')
                    case '77746':
                        self.sendJsonFromFile('goalfiles/77746.json')

                    case _: self.notFound()

            case 'goalfiles':
                self.sendJsonFromFile('goalfiles/goalfiles.json')

            case 'countgoalfiles':
                self.sendText('123')

            case 'countgoalfilesbytype':
                self.sendJsonFromFile('goalfiles/countgoalfilesbytype.json')

            case 'goalfilerevisions':
                self.sendJsonFromFile('goalfiles/goalfilerevisions.json')

            case 'goalfilestatus':
                self.sendJsonFromFile('goalfiles/goalfilestatus.json')

            case 'goalfiletypes':
                self.sendJsonFromFile('goalfiles/goalfiletypes.json')

            case 'organizationunits':
                self.sendJsonFromFile('goalfiles/organizationunits.json')

            case 'supervisororganizationunits':
                self.sendJsonFromFile('goalfiles/supervisororganizationunits.json')

            case 'file-test':
                match self.requestData.path.get(1):
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
