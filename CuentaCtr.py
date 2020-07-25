from dao import Dao
from CuentaModelo import CuentaM

class cuentaControl:
    def __init__(self, cuentas=None):
        self.cuenta=cuentas

    def consulta(self, buscar):
        objDao=Dao()
        return objDao.consultarC(buscar)

    def ingresar(self, cuentas):
        objDao=Dao()
        return objDao.ingresarC(cuentas)

    def modificar(self, cuentas):
        objDao=Dao()
        return objDao.modificarC(cuentas)

    def eliminar(self, cuentas):
        objDao=Dao()
        return objDao.eliminarC(cuentas)