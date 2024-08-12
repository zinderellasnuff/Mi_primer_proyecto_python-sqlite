import datetime
import hashlib
import usuarios.conexion as conexion

connect = conexion.conectar()
database = connect[0]
cursor  = connect[1]

class Usuario:

    def __init__(self, nombre, apellidos, email, password): # Es el primer metodo que se ejecuta cuando creamos un obejto
        # se encarga de inicializar y dar un valor a diferentes propiedades de clases
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password
    
    def registrar (self): 
        fecha = datetime.datetime.now()

        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        # sql: Para guardar mis consultas   id  name ap  @  con  fecha
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        # % para sustituir esto por datos que tenga en una tupla
        # tupla
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)
        
        try:
            cursor.execute(sql, usuario) # Ejecuta la consulta sql
            database.commit() # commit : permite ejecutar todas estas consultas y que se guarden en la base de datos

            result = [cursor.rowcount, self]
        except:
            result = [0, self]
        
        return result

    def identificar (self):

        # Consulta para comprobar si existe el usuario
        sql =  "SELECT * FROM usuarios WHERE email = %s AND password = %s"

        # Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode("utf8"))

        # Datos para la consulta
        usuario = (self.email, cifrado.hexdigest())


        cursor.execute (sql , usuario)
        result = cursor.fetchone() # fechone para solo un usario

        return result