class ServerConfig:
    @property
    def host(self) -> str:
        return self.__host
    @property
    def port(self) -> int:
        return self.__port

    def __init__(self, host: str, port: int):
        self.__host = host
        self.__port = port

    def __str__(self):
        return str({
            'host': self.__host,
            'port': self.__port
        })

    def __repr__(self):
        return self.__str__()
