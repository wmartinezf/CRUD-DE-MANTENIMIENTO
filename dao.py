import sys
from conexion import Conector

class Dao(Conector):
    def __init__(self):
        super().__init__()

    def consultarG(self, buscar):
        result= False
        try:
            sql="Select id, descripcion from grupo where descripcion like '%" + \
                str(buscar) + "%' order by id"
            self.conectar()
            self.conector.execute(sql)
            result=self.conector.fetchall()
            self.conn.commit()
        except Exception as e:
            print("Error al momento de consultar", e)
            self.conn.rollback()
        finally:
            self.cerrar()
        return result

    def ingresarG(self, grupos):
        correcto=True
        try:
            sql="insert into grupo (descripcion) values (%s)"
            self.conectar()
            self.conector.execute(sql,(grupos.descrip))
            self.conn.commit()
        except Exception as e:
            print("Error al momento de insertar", e)
            correcto=False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    def modificarG(self, grupos):
        correcto=True
        try:
            sql='Update grupo set descripcion = %s where id=%s'
            self.conectar()
            self.conector.execute(sql,(grupos.descrip, grupos.Identificacion))
            self.conn.commit()
        except Exception as e:
            print("Error al momento de modificar", e)
            correcto=False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    def eliminarG(self, grupos):
        correcto=True
        try:
            sql='delete from grupo where id= %s'
            self.conectar()
            self.conector.execute(sql, (grupos.Identificacion))
            self.conn.commit()
        except Exception as e:
            print("Error al momento de eliminar", e)
            correcto=False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    def consultarC(self, buscar):
        result= False
        try:
            sql="Select id, codigo, grupo, descripcion, naturaleza, estado from Pcuenta where codigo like '%" + \
                str(buscar) + "%' order by id"
            self.conectar()
            self.conector.execute(sql)
            result=self.conector.fetchall()
            self.conn.commit()
        except Exception as e:
            print("Error en la consulta", e)
            self.conn.rollback()
        finally:
            self.cerrar()
        return result

    def ingresarC(self, cuentas):
        correcto=True
        try:
            sql="insert into Pcuenta (codigo, grupo, descripcion, naturaleza, estado) values (%s,%s,%s,%s,%s)"
            self.conectar()
            self.conector.execute(sql,(cuentas.Codigo, cuentas.Grupo, cuentas.Descripcion, cuentas.Naturaleza, cuentas.Estado))
            self.conn.commit()
        except Exception as e:
            print("Error al momento de insertar", e)
            correcto=False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    def modificarC(self, cuentas):
        correcto=True
        try:
            sql='Update Pcuenta set codigo = %s, grupo=%s, descripcion=%s, naturaleza=%s, estado=%s where id=%s'
            self.conectar()
            self.conector.execute(sql,(cuentas.Codigo, cuentas.Grupo, cuentas.Descripcion, cuentas.Naturaleza, cuentas.Estado,cuentas.Identificacion))
            self.conn.commit()
        except Exception as e:
            print("Error al momento de modificar", e)
            correcto=False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto

    def eliminarC(self, cuentas):
        correcto=True
        try:
            sql='delete from Pcuenta where id= %s'
            self.conectar()
            self.conector.execute(sql, (cuentas.Identificacion))
            self.conn.commit()
        except Exception as e:
            print("Error al momento de eliminar", e)
            correcto=False
            self.conn.rollback()
        finally:
            self.cerrar()
        return correcto


