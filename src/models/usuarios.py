from database.main import initConn
from security.main import *

def getUsuarios():
  try:
    conn = initConn()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE eliminado=false')
    usuarios = cursor.fetchall()
    cursor.close()
    conn.close()

    return usuarios
  except Exception as e:
    print("Error al obtener los usuarios: ",e)
    return None
  
def userExists(user_name, correo):
  try:
    conn = initConn()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE (user_name=%s OR correo=%s) AND eliminado=false', (user_name, correo))
    usuario = cursor.fetchone()
    cursor.close()
    conn.close()

    if usuario:
      return True
    return False
  except Exception as e:
    print("Error al verificar si el usuario existe: ",e)
    return False

def registrarUsuario(datos):
  try:
    # *Comprueba si el usuario existe
    if userExists(datos.get('user_name'), datos.get('email')):
      return False

    conn = initConn()
    cursor = conn.cursor()
    query = """
      INSERT INTO usuarios(id, nombre, apepat, apemat, user_name, correo, password)
      VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (
      getId(),
      datos.get('name'),
      datos.get('fLastName'),
      datos.get('sLastName'),
      datos.get('user_name'),
      datos.get('email'),
      hashPassword(datos['password'])
    )

    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return True
  except Exception as e:
    print("Error al registrar el usuario: ",e)
    return False

