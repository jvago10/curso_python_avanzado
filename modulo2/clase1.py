"""
PROGRAMA PARA GUARDAR DATOS DE MI PC
"""
import platform
import socket


def guardar_pc_info():
    pc_data = "========== INFO DE PC ==========\n"
    pc_data += "SISTEMA OPERATIVO :" + platform.system()
    pc_data += ' ' + platform.version() + "\n"
    pc_data += "ARQUITECTURA :" + platform.machine() + "\n"
    pc_data += "PROCESADOR :" + platform.processor() + "\n"
    pc_data += "HOSTNAME :" + socket.gethostname() + "\n"
    pc_data += "IP :" + socket.gethostbyname(socket.gethostname()) + "\n"
    pc_file = open('pc.txt', 'w')
    pc_file.write(pc_data)
    pc_file.close()
    print("El archivo se guardó con éxito")


def leer_pc_info():
    try:
        pc_file = open('pc.txt', 'r')
        pc_data = pc_file.read()
        print(pc_data)
        pc_file.close()
    except FileNotFoundError:
        print("No se encontró el archivo")


if __name__ == '__main__':
    guardar_pc_info()
    leer_pc_info()
