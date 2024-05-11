from database.main import initConn
from security.main import *

def getMensajes():
  try:
    conn = initConn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM contactos WHERE eliminado=false ORDER BY created_at DESC")
    mensajes = cursor.fetchall()
    cursor.close()
    conn.close()

    return mensajes
  except Exception as e:
    print("Error al obtener todos los mensajes, getMensajes(): ",e)
    return None
  
def getMensaje(id):
  try:
    conn = initConn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM contactos WHERE id=%s AND eliminado=false", (id,))
    mensaje = cursor.fetchone()
    cursor.close()
    conn.close()

    return mensaje
  except Exception as e:
    print("Error al obtener el mensaje, getMensaje(): ",e)
    return None
  
def createMensaje(data):
  try:
    conn = initConn()
    cursor = conn.cursor()
    query = """
      INSERT INTO contactos (id, correo, motivo, tipo_contacto, categoria, mensaje, id_usuario)
      VALUES (%s, %s, %s, %s, %s, %s, %s)
    """ 
    values = (
      getId(), data.get('email'),
      data.get('motivo'), data.get('tipo'),
      data.get('categoria'), data.get('cuerpo'),
      data.get('id_user')
    )
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    
    return True
  except Exception as e:
    print("Error al crear el mensaje, createMensaje(): ",e)
    return None

# *Metodo para evitar SPAM, verifica que no existan mas de 3 mensajes de la misma persona en menos de 5 minutos
def checkSpam(data):
  try:
    conn = initConn()
    cursor = conn.cursor()
    query = """
      SELECT COUNT(*) FROM contactos
      WHERE correo=%s AND id_usuario=%s AND created_at >= NOW() - INTERVAL 5 MINUTE
    """
    cursor.execute(query, (data.get('email'), data.get('id_user')))
    count = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if count[0] >= 3:
      return True
    return False
  except Exception as e:
    print("Error al verificar spam, checkSpam(): ",e)
    return None
  
def deleteMensaje(id):
  try:
    conn = initConn()
    cursor = conn.cursor()
    query = "UPDATE contactos SET eliminado=true WHERE id=%s"
    cursor.execute(query, (id,))
    conn.commit()
    cursor.close()
    conn.close()
    
    return True
  except Exception as e:
    print("Error al eliminar el mensaje, deleteMensaje(): ",e)
    return None