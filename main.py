from paciente import Paciente
from medico import Medico

usuario = [Paciente("Rocío", "Staltari", 12345678, 2945414794, "rocio@gmail.com", "12345678")]
usuario_activo = []
medicos = [Medico("Juan", "Pérez", 87654321, 2945123456, "juan@gmail.com", "Traumatólogo", 2)]

titulo_programa = "SISTEMA DE GESTIÓN DE TURNOS"
print(f"╔═{"═" * len(titulo_programa)}═╗")
print(f"║ {" " * len(titulo_programa)} ║")
print(f"║ {titulo_programa} ║")
print(f"║ {" " * len(titulo_programa)} ║")
print(f"╚═{"═" * len(titulo_programa)}═╝")

print("Elija una opción:")
print("1. Registrarse")
print("2. Iniciar sesión")
opcion = input("→ ")

if opcion == "2":
    correo = input("Correo electrónico: ")
    contraseña = input("Contraseña: ")
    for i in range(0, len(usuario)):
        if usuario[i].get_correo() == correo and usuario[i].get_contraseña() == contraseña:
            usuario_activo.append[usuario[i].get_nombre(), usuario[i].get_apellido, usuario[i].get_dni]
            while True:
                print("Elija una opción:")
                print("1. Lista de turnos por médico")
                print("2. Agendar tunro")
                print("3. Mostrar usuario activo")
                res = input("→ ")
                opcion(res)
        else:
            print("Los datos no son válidos, inténtelo de nuevo o regístrese.")
elif opcion == "1":
    print("Ingrese los datos:")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("DNI: ")
    telefono = input("Teléfono: ")
    correo = input("Correo electrónico: ")
    contraseña = input("Contraseña: ")
    usuario.append(Paciente(nombre, apellido, dni, telefono, correo, contraseña))
    index = len(usuario) - 1
    usuario_activo = [usuario[index].get_nombre, usuario[index].get_apellido, usuario[index].get_dni]
    while True:
        print("Elija una opción:")
        print("1. Lista de turnos por médico")
        print("2. Agendar tunro")
        print("3. Mostrar usuario activo")
        res = input("→ ")
        opcion(res)

def opcion(res):
    if res == "1":
        pass