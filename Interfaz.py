from GrupoCtr import grupoControl
from GrupoModelo import GrupoM
from CuentaCtr import cuentaControl
from CuentaModelo import CuentaM
from funciones import menu
import os
GrupoCtr=grupoControl()
CuentaCtr=cuentaControl()


def insertarG(rango):
    for i in range(int(rango)):
        descripc=input('Ingrese descripcion: ')
        cli=GrupoM(descrip=descripc)
        if GrupoCtr.ingresar(cli):
            print('Registro grabado correctamente')
        else:
            print('Error al grabar')

def modificarG():
    ide=input('Ingrese id: ')
    descrip=input('Ingrese descripcion: ')
    cli=GrupoM(ide=ide, descrip=descrip)
    if GrupoCtr.modificar(cli):
        print('Registro modificado correctamente')
    else:
        print('Error al modificar')

def eliminarG():
    ide=input('Ingrese id: ')
    cli=GrupoM(ide=ide)
    if GrupoCtr.eliminar(cli):
        print('Registro eliminado correctamente')
    else:
        print('Error al eliminar')


def consultarG():
    buscar=input('Ingrese grupo:')
    cli=GrupoCtr.consulta(buscar)
    print('Id  Descripcion')
    for registro in cli:
        print('{:4}{:6} '.format(registro[0],registro[1]))


def insertarC(rango):
    for i in range(int(rango)):
        ide=input('Ingrese código: ')
        grup=input('Ingrese grupo: ')
        descrip=input('Ingrese descripcion: ')
        naturalez=input('Ingrese naturaleza: ')
        estad=input('Ingrese estado: ')
        cli=CuentaM(ide=ide, grup=grup, descrip=descrip, naturalez=naturalez, estad=estad)
        if CuentaCtr.ingresar(cli):
            print('Registro grabado correctamente')
        else:
            print('Error al grabar')

def modificarC():
    ide=input('Ingrese id: ')
    codig=input('Ingrese código: ')
    grup=input('Ingrese grupo: ')
    descrip=input('Ingrese descripcion: ')
    naturalez=input('Ingrese naturaleza: ')
    estad=input('Ingrese estado: ')
    cli=CuentaM(ide=ide, codig=codig, grup=grup, descrip=descrip, naturalez=naturalez, estad=estad)
    if CuentaCtr.modificar(cli):
        print('Registro modificado correctamente')
    else:
        print('Error al modificar')

def eliminarC():
    consultarC()
    ide=input('Ingrese id: ')
    cli=CuentaM(ide=ide)
    if CuentaCtr.eliminar(cli):
        print('Registro eliminado correctamente')
    else:
        print('Error al eliminar')


def consultarC():
    buscar=input('Ingrese cuenta:')
    cli=CuentaCtr.consulta(buscar)
    print(' Id  Codigo  grupo  Descripcion  Naturaleza  Estado')
    for registro in cli:
        print('{:1}         {:1}{:6}    {:9}        {:5}{:6}'.format(registro[0],registro[1],registro[2],registro[3],registro[4],registro[5]))


def ejecutar():
    opc=''
    while True:
        opc=str(menu(['Grupo de Cuentas','Plan de Cuentas','Salir'],'MENU PRINCIPAL ¯\_( ͡❛ ͜ʖ ͡❛)_/¯ '))
        if opc=='0':
            while True:
             try:
                opc=str(menu(['Ingresar','Consultar','Modificar','Eliminar','Retornar Menu Principal'],'MENU GRUPO'))
                if opc=='0':
                    print('\n<<<Ingresar>>>')
                    valor=input('Cantidad de datos: ')
                    insertarG(valor)
                elif opc=='1':
                    print('\n<<<Consulta>>>')
                    consultarG()
                elif opc=='2':
                    print('\n<<<Modificación>>>')
                    consultarG()
                    modificarG()
                elif opc=='3':
                    print('\n<<<Eliminación>>>')
                    consultarG()
                    eliminarG()
                elif opc=='4':
                    ejecutar()
             except:
                 print('\n<<<Ingrese solo valores validos...>>>')
        elif opc=='1':
            while True:
             try:
                opc=str(menu(['Ingresar','Consultar','Modificar','Eliminar','Retornar Menu Principal'],'MENU CUENTAS'))
                if opc=='0':
                    print('\n<<< Ingresar >>>')
                    cantidad=input('Cantidad de datos: ')
                    insertarC(cantidad)
                elif opc=='1':
                    print('\n<<< Consulta >>>')
                    consultarC()
                elif opc=='2':
                    print('\n<<<Modificación>>>')
                    consultarC()
                    modificarC()
                elif opc=='3':
                    print('\n<<<Eliminación>>>')
                    consultarC()
                    eliminarC()
                elif opc=='4':
                   ejecutar()
             except:
                 print('\n<<<Ingrese solo valores validos...>>>')
        elif opc=='2':
            print('\n<<<Salir>>>')
        break
ejecutar()