import usuarios.usuario as modelo # alias 
import notas.acciones 

class Acciones:

    def registro(self):
        print("\nBienvenido, vamos a registrarte en el sistema")

        nombre = input("¿Cual es tu nombre? :")
        apellidos = input("¿Cual es tu apellido? :")
        email = input("Indroduce tu email :")
        password = input("Indroduce tu contraseña :")

        usuario = modelo.Usuario(nombre,apellidos,email,password)
        registro = usuario.registrar() # Registro de usuarios

        if registro[0] >= 1: #si es mayor igual a uno se habra registrado el usario 
            print(f"\nPerfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("No te has registrado correctamente")

    def login (self):
        print("\nIdentificate en el sistema")

        try :
            email = input("Indroduce tu email :")
            password = input("Indroduce tu contraseña :")

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido {login[1]}, te has registrado en el {login[5]}")
                self.proximasAcciones (login)
    
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login incorrecto, intentalo mas tarde")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles :
        - Crear notas (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar nota (eliminar)
        - Salir (salir)
""")
        opccion = input("¿Que quieres hacer?:")
        hazEl = notas.acciones.Acciones()

        if opccion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif opccion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif opccion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
            
        elif opccion == "salir":
            print(f"ok {usuario[1]}, hasta pronto")
            exit()