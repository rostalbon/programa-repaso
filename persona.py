class Persona:
    def __init__(self, nombre, apellido, dni, telefono, correo):
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._telefono = telefono
        self._correo = correo
    def get_nombre(self):
        return self._nombre
    def get_apellido(self):
        return self._apellido
    def get_dni(self):
        return self._dni
    def get_telefono(self):
        return self._telefono
    def get_correo(self):
        return self._correo