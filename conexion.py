import sys
import pymysql
class Conector():
    def __init__(self, server='localhost', port=3306, usuario='root', password='', basedato='Grupo_Cuentas'):
        self.__server=server
        self.__usuario=usuario
        self.__password=password
        self.__basedato=basedato
        self.__con=''
        self.__conector=''

    def conectar(self):
        try:
            self.__conn=pymysql.connect(
                host=self.__server ,user=self.__usuario, passwd=self.__password, db=self.__basedato
            )
            self.__conector=self.__conn.cursor()
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
            print("Error en la conexion",e)
            sys.exit(1)

    def cerrar(self):
        self.__conn.close()
        self.__conector.close()

    @property
    def conector(self):
        return self.__conector

    @property
    def conn(self):
        return self.__conn
