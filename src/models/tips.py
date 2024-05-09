from database.main import initConn
from security.main import *

def getTips():
  try:
    conn = initConn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM tips WHERE eliminado=false ORDER BY created_at, likes DESC')
    tips = cursor.fetchall()
    cursor.close()
    conn.close()

    return tips
  except Exception as e:
    print("Error al obtener los tips: ",e)
    return None
  
def getUserTips(id):
  try:
    conn = initConn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM tips WHERE id_usuario=%s AND eliminado=false ORDER BY created_at, likes DESC', (id,))
    tips = cursor.fetchall()
    cursor.close()
    conn.close()

    return tips
  except Exception as e:
    print("Error al obtener los tips del usuario: ",e)
    return None
  
def createTip(data):
  try:
    conn = initConn()
    cursor = conn.cursor()
    query = """
      INSERT INTO tips(id, id_usuario, titulo, descripcion)
      VALUES (%s, %s, %s, %s)
    """
    values = (
      getId(),
      data.get('id_user'),
      data.get('title'),
      data.get('descrip'),
    )

    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()
    return True
  except Exception as e:
    print("Error al crear el tip: ",e)
    return False
  
def deleteTip(id, id_user):
  try:
    conn = initConn()
    cursor = conn.cursor()
    query = """
      UPDATE tips SET eliminado=true WHERE id=%s AND id_usuario=%s AND eliminado=false
    """
    values = (id, id_user)
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

    return True
  except Exception as e:
    print("Error al eliminar el tip: ",e)
    return False
  
def likeTip(id):
  try:
    conn = initConn()
    cursor = conn.cursor()
    query = """
      UPDATE tips SET likes=likes+1 WHERE id=%s AND eliminado=false
    """
    cursor.execute(query, (id,))
    conn.commit()
    cursor.close()
    conn.close()

    return True
  except Exception as e:
    print("Error al dar like al tip: ",e)
    return False
  
def dislikeTip(id):
  try:
    conn = initConn()
    cursor = conn.cursor()
    query = """
      UPDATE tips SET dislikes=dislikes+1 WHERE id=%s AND eliminado=false
    """
    cursor.execute(query, (id,))
    conn.commit()
    cursor.close()
    conn.close()

    return True
  except Exception as e:
    print("Error al quitar like al tip: ",e)
    return False
  
def reportarTip(id):
  try:
    conn = initConn()
    cursor = conn.cursor()
    query = """
      UPDATE tips SET reportes=reportes+1 WHERE id=%s AND eliminado=false
    """
    cursor.execute(query, (id,))
    conn.commit()
    cursor.close()
    conn.close()

    return True
  except Exception as e:
    print("Error al reportar el tip: ",e)
    return False
  
def editTip(data):
  try:
    conn = initConn()
    cursor = conn.cursor()
    query = """
      UPDATE tips SET titulo=%s, descripcion=%s, last_mod=NOW() WHERE id=%s AND eliminado=false
    """
    values = (data.get('title'), data.get('descrip'), data.get('id'))
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

    return True
  except Exception as e:
    print("Error al editar el tip: ",e)
    return False