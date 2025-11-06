from consultorio import Consultorio

class Hospital:
    def __init__(self, nombre, direccion, cant_consultorios, numero):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__cant_consultorios = cant_consultorios
        self.__consultorio = Consultorio(numero) #Composición