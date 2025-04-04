from http_server.base.model.HttpMethod import HttpMethod


class Request:
    @property
    def method(self) -> HttpMethod:
        return self.__method
    @property
    def path(self) -> dict[int, str]:
        return self.__pathArray
    @property
    def pathString(self) -> str:
        return self.__pathString
    @property
    def queryParams(self) -> dict[str, any]:
        return self.__queryParams

    def __init__(self, path: str, method: HttpMethod):
        self.__method = method
        pathAndQueryParams = path.split('?')
        self.__pathString = pathAndQueryParams[0].strip('/').strip('\\')
        self.__pathArray = {}
        for segment in self.__pathString.split('/'):
            if len(segment) > 0:
                self.__pathArray[len(self.__pathArray)] = segment
        self.__queryParams = {}
        if len(pathAndQueryParams) > 1:
            queryString = pathAndQueryParams[1]
            paramValuePairs = queryString.split('&')
            for paramValuePair in paramValuePairs:
                paramValue = paramValuePair.split('=')
                if len(paramValue) == 1:
                    self.__queryParams[paramValue[0]] = True
                else:
                    if self.__queryParams.get(paramValue[0]) is None:
                        self.__queryParams[paramValue[0]] = paramValue[1]
                    else:
                        if isinstance(self.__queryParams.get(paramValue[0]), list):
                            self.__queryParams[paramValue[0]].append(paramValue[1])
                        else:
                            self.__queryParams[paramValue[0]] = [self.__queryParams.get(paramValue[0]), paramValue[1]]

    def __str__(self):
        return f"Request({self.method.value} {self.pathString} queryParams={self.queryParams})"




