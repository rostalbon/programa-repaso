from persona import Persona

class Paciente(Persona):
    def __init__(self, nombre, apellido, dni, telefono, correo, contraseña, legajo=""):
        super().__init__(nombre, apellido, dni, telefono, correo)
        self._contraseña = contraseña
        self._legajo = legajo
    def get_contraseña(self):
        return self._contraseña