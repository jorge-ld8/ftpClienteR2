import os.path
import sys
from ftplib import FTP, error_perm, all_errors, error_reply
from os import path as p
from time import sleep
from functools import partial


def uniquify(path):
    filename, extension = p.splitext(path)
    counter = 1
    returnPath = path

    while p.exists(returnPath):
        returnPath = f'{filename}({counter}){extension}'
        counter += 1

    return returnPath


def procesarArchivo(archivo, nombre):
    with open(uniquify(nombre), "w") as f:
        print(archivo)
        f.write(archivo)

def menu(ftpcliente: FTP):
    # Darle la bienvenida al usuario
    print("Bienvenido al servidor FTP Genesis I")
    while True:
        print("\tIntroduzca el numero segun la opcion")
        print("\t1.Ver estructura")
        print("\t2.Bajar archivo")
        print("\t3.Subir archivo")
        print("\t4.Borrar archivo")
        print("\t5.Crear directorio")
        print("\t6.Eliminar directorio")
        print("\t7.Compartir archivo con otro usuario")
        print("\t8.Cambiar contraseña")
        print("\t0.Salir")
        resp = input("\tOpcion: ")
        if resp == "1":
            print("\tCONTENIDO")
            for name, facts in ftpcliente.mlsd(facts=["size", "type"]):
                print("\t\t" + name + ": " + facts["type"] + " " + facts["size"] + "B")
        elif resp == "2":
            def remove_last_line_from_string(s):
                return
            nombreArchivo = input("Introduzca el nombre del archivo que desea obtener: ")
            try:
                wantedFile = ftpcliente.retrlines(f'RETR {nombreArchivo}', lambda x: procesarArchivo(x, nombreArchivo))
                print(f'Archivo guardado exitosamente. Lo puede encontrar en {os.getcwd()}')
            except error_perm:
                print("\tArchivo no conseguido. Intente nuevamente")
        elif resp == "3":
            nombreArchivo = input("Introduzca el nombre del archivo que desea subir: ")
            try:
                f = open(nombreArchivo, "rb")
                ftpcliente.storlines(f'STOR {nombreArchivo}', f)
                print("Archivo subido exitosamente!")
                f.close()
            except IOError:
                print("Ha ocurrido un error. Intente nuevamente")
            except error_perm as e:
                print(e)
        elif resp == "4":
            nombreArchivo = input("Introduzca el nombre del archivo que desea borrar: ")
            try:
                ftpcliente.delete(nombreArchivo)
                print("Archivo borrado exitosamente!")
            except error_perm:
                print("Ha ocurrido un error de permisos. Intente nuevamente")
            except error_reply:
                print("Ha ocurrido un error inesperado. Intente nuevamente")
            except Exception as e:
                print(e)
        elif resp == "5":
            nombreDirectorio = input("Introduzca el nombre del directorio que desea crear: ")
            try:
                ftpcliente.mkd(nombreDirectorio)
                print("Directorio creado exitosamente!")
            except Exception as e:
                print(e)
        elif resp == "6":
            nombreDirectorio = input("Introduzca el nombre del directorio que desea borrar: ")
            try:
                ftpcliente.rmd(nombreDirectorio)
                print("Directorio eliminado exitosamente")
            except Exception as e:
                print(e)
        elif resp == "7":
            filename = input("Que archivo desea compartir: ")
            user = input("A que usuario se lo desea compartir: ")
            try:
                ftpcliente.sendcmd(f'SITE SHAREFILE {filename} {user}')
            except Exception as e:
                print(e)
        elif resp == "8":
            # pedir la contrasena
            pswd = input("Introduzca la nueva contraseña: ")
            # volver a pedirla
            pswd2 = input("Introduzca la contraseña nuevamente: ")
            # verificar que sean iguales
            if pswd == pswd2:
                oldpswd = input("Introduzca la contraseña anterior:")
                try:
                    ftpcliente.sendcmd(f'SITE PSWD {oldpswd} {pswd}')
                except Exception as e:
                    print(e)
            else:
                print("ERROR. Intente nuevamente")
        elif resp == "0":
            ftpcliente.close()
            break
        input("")


def main():
    contfallos = 0
    while True:
        try:
            ftp = FTP('')
            # PARAMETROS
            NUM_MAX_CONEXIONES = 3
            cont = 0
            while cont < NUM_MAX_CONEXIONES: # LOGIN
                try:
                    host = input("Ingrese el host: ")
                    port = int(input("Ingrese el puerto: "))

                    # Login
                    user = input("Ingrese su usuario: ")
                    password = input("Ingrese su contraseña: ")
                    ftp.connect(host, port)
                    ftp.login(user=user, passwd=password)
                    cont = 0
                    # loop en el que consiste la aplicacion
                    menu(ftp)
                    return
                except error_perm as e:
                    cont += 1
                    print(e)
                except EOFError:
                    print("Numero maximo de logins alcanzado")
        except ConnectionRefusedError:
            while True:
                print("El servidor no está activo. Tratando reconexion")
                contfallos += 1
                if contfallos == 3:
                    break
                sleep(4)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
