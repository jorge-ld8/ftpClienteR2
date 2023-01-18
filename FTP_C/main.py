import os.path
from ftplib import FTP, error_perm, all_errors, error_reply
from os import path as p
from time import sleep
import ntpath

def uniquify(path):
    filename, extension = p.splitext(path)
    counter = 1
    returnPath = path

    while p.exists(returnPath):
        returnPath = f'{filename}({counter}){extension}'
        counter += 1

    return returnPath


def c_sesion(ftpcliente: FTP):
    # Darle la bienvenida al usuario
    print("Bienvenido al servidor FTP Genesis I")
    ftpcliente.close()
    print("cerrado")

    '''while True:
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
                print("\t\t" + name + ": " + facts["type"] + " " + facts["size"] + "KB")
        elif resp == "2":
            nombreArchivo = input("Introduzca el nombre del archivo que desea obtener: ")
            try:
                wantedFile = ftpcliente.retrlines(f'RETR {nombreArchivo}')
                with open(uniquify(nombreArchivo), "w") as f:
                    f.write(wantedFile)
                print(f'Archivo guardado exitosamente. Lo puede encontrar en {os.getcwd()}')
            except error_perm:
                print("\tArchivo no conseguido. Intente nuevamente")
        
        
        
        elif resp == "7":
            filename = input("Que archivo desea compartir: ")
            user = input("A que usuario se lo desea compartir: ")
            try:
                ftpcliente.sendcmd(f'SITE SHAREFILE {filename} {user}')
            except Exception as e:
                print(e)
        '''

def subir_arch(ftpcliente: FTP, nombreArchivo):
    #nombreArchivo = input("Introduzca el nombre del archivo que desea subir: ")
    #aux = path_leaf(nombreArchivo)
    try:
        f = open(nombreArchivo, "rb")
        ftpcliente.storlines(f'STOU {nombreArchivo}', f)
        print("Archivo subido exitosamente!")
        f.close()
    except IOError:
        print("Ha ocurrido un error. Intente nuevamente")
    # ftpcliente.

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def crear_dir(ftpcliente: FTP, nombreDirectorio):
    #nombreDirectorio = input("Introduzca el nombre del directorio que desea crear: ")
    try:
        ftpcliente.mkd(nombreDirectorio)
        print("Directorio creado exitosamente!")
    except Exception as e:
        print(e)

def elim_dir(ftpcliente: FTP, nombreDirectorio):
    #nombreDirectorio = input("Introduzca el nombre del directorio que desea borrar: ")
    try:
        ftpcliente.rmd(nombreDirectorio)
        print("Directorio eliminado exitosamente")
    except Exception as e:
        print(e)

def cambio_contra(ftpcliente: FTP, pswd, oldpswd):
    '''# pedir la contrasena
    pswd = input("Introduzca la nueva contraseña: ")
    # volver a pedirla
    pswd2 = input("Introduzca la contraseña nuevamente: ")
    # verificar que sean iguales
    if pswd == pswd2:
        oldpswd = input("Introduzca la contraseña anterior:")'''
    try:
        ftpcliente.sendcmd(f'SITE PSWD {oldpswd} {pswd}')
    except Exception as e:
        print(e)
    '''else:
        print("ERROR. Intente nuevamente")'''

def ver_arch(ftpcliente: FTP):
    archivos = []
    for name, facts in ftpcliente.mlsd(facts=["size", "type"]):
        archivos.append(name + ": " + facts["type"] + " " + facts["size"] + "KB")
        print("\t\t" + name + ": " + facts["type"] + " " + facts["size"] + "KB")
    return archivos

def elim_arch(ftpcliente: FTP, nombreArchivo):
    #nombreArchivo = input("Introduzca el nombre del archivo que desea borrar: ")
    try:
        ftpcliente.delete(nombreArchivo)
        print("Archivo borrado exitosamente!")
    except error_perm:
        print("Ha ocurrido un error de permisos. Intente nuevamente")
    except error_reply:
        print("Ha ocurrido un error inesperado. Intente nuevamente")
    except Exception as e:
        print(e)

def bajar_arch(ftpcliente: FTP, nombreArchivo):
    #nombreArchivo = input("Introduzca el nombre del archivo que desea obtener: ")
    try:
        wantedFile = ftpcliente.retrlines(f'RETR {nombreArchivo}')
        with open(uniquify(nombreArchivo), "w") as f:
            f.write(wantedFile)
        return f'Archivo guardado exitosamente. Lo puede encontrar en {os.getcwd()}'
    except error_perm:
        print("\tArchivo no conseguido. Intente nuevamente")

def comp_arch(ftpcliente: FTP, filename, user):
    #filename = input("Que archivo desea compartir: ")
    #user = input("A que usuario se lo desea compartir: ")
    print(filename)
    print(user)
    try:
        ftpcliente.sendcmd(f'SITE SHAREFILE {filename} {user}')
        return "Archivo compartido satisfactoriamente!!"
    except Exception as e:
        print(e)
    

def main(h, p, u, ps):
    contfallos = 0
    while True:
        try:
            ftp = FTP('')
            # PARAMETROS
            NUM_MAX_CONEXIONES = 3
            cont = 0
            while cont < NUM_MAX_CONEXIONES: # LOGIN
                try:
                    host = h#input("Ingrese el host: ")
                    port = p#int(input("Ingrese el puerto: "))

                    # Login
                    user = u#input("Ingrese su usuario: ")
                    password = ps#input("Ingrese su contraseña: ")
                    ftp.connect(host, port)
                    ftp.login(user=user, passwd=password)
                    cont = 0
                    # loop en el que consiste la aplicacion
                    #menu(ftp)
                    return ftp
                except error_perm:
                    cont += 1
                    print("Login failed")
                except EOFError:
                    print("Numero maximo de logins alcanzado")
        except ConnectionRefusedError:
            print("El servidor no está activo. Intente nuevamente.")
            contfallos += 1
            if contfallos == 5:
                break
            sleep(4)


# Press the green button in the gutter to run the script.
'''if __name__ == '__main__':
    main()'''

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
