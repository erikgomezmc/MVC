import mariadb as sql 

class ConexionesDB():
    def __init__(self):
        self.__host = "localhost"
        self.__port = 3307
        self.__user = "root"
        self.__password = ""
        self.__database = "ejemplo"
        self.__connection = None

    def getconection(self):
        return self.__conection
    
    def crearConexion(self):
        self.__connection = sql.connect(
            host = self.__host,
            user = self.__user,
            password = self.__password,
            port = self.__port,
            database = self.__database
        )
    def cerrarConexion(self):
        if self.__connection:
            self.__connection = None    