from http_server.base.model.HttpMethod import HttpMethod


class Request:
    @property
    def method(self) -> HttpMethod:
        return self.__method
    @property
    def path(self) -> list[str]:
        return self.__pathArray
    @property
    def pathString(self) -> str:
        return self.__pathString
    @property
    def queryParams(self) -> dict[str, any]:
        return self.__queryParams

    def __init__(self, path: str, method: HttpMethod):
        self.__method = method
        tmp = path.split('?')
        self.__pathString = tmp[0].strip('/').strip('\\')
        self.__pathArray = [segment for segment in self.__pathString.split('/') if len(segment) > 0]
        self.__queryParams = {}
        if len(tmp) > 1:
            queryString = tmp[1]
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





