from dao import Dao
from GrupoModelo import GrupoM

class grupoControl:
    def __init__(self, grupos=None):
        self.grupo=grupos

    def consulta(self, buscar):
        objDao=Dao()
        return objDao.consultarG(buscar)

    def ingresar(self, grupos):
        objDao=Dao()
        return objDao.ingresarG(grupos)

    def modificar(self, grupos):
        objDao=Dao()
        return objDao.modificarG(grupos)

    def eliminar(self, grupos):
        objDao=Dao()
        return objDao.eliminarG(grupos)
