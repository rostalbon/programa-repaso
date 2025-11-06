from persona import Persona

class Medico(Persona):
    def __init__(self, nombre, apellido, dni, telefono, correo, especialidad, consultorio, matricula = ""):
        super().__init__(nombre, apellido, dni, telefono, correo)
        self._especialidad = especialidad
        self._consultorio = consultorio
        self._matricula = matricula