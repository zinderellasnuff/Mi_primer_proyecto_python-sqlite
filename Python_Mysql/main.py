"""
Proyecto-python y Mysql :
-Abrir asistente
-Login o registro
-Si elegimos registro, creara un usuario en la bbdd
-Si elegimos login, identifica al usuario y nos pregunta
-Crear nota, mostrar notas, borrarlas.
"""

from usuarios import acciones #Importar mi modulo y dentro de este modulo puedo crear objeto de acciones

print("""
Acciones disponibles :
      -registro
      -login
""")

hazEl = acciones.Acciones() # Creando mi objeto o instanciando mi clase
opcion = input("¿Que desea hacer? :")

# Menu de opcciones 
if opcion == "registro":
    hazEl.registro()

elif opcion == "login":
    hazEl.login()