from database.main import initConn
from security.main import *

def getPosts():
  try:
    conn = initConn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM publicaciones WHERE eliminado=false ORDER BY created_at DESC")
    posts = cursor.fetchall()
    conn.close()

    return posts
  except Exception as e:
    print("Error al obtener los posts: ",e)
    return None

def getPost(id):
  try:
    conn = initConn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM publicaciones WHERE id=%s AND eliminado=false", (id,))
    post = cursor.fetchone()
    conn.close()

    return post
  except Exception as e:
    print(f"Error al obtener el post con el id: {id}: {e}")
    return None
  
def getUserPost(id):
  try:
    conn = initConn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM publicaciones WHERE id_usuario=%s AND eliminado=false", (id,))
    posts = cursor.fetchall()
    conn.close()

    return posts
  except Exception as e:
    print(f"Error al obtener los posts de un usuario con el id: {id}: {e}")
    return None
  
def createPost(data):
  try:
    conn = initConn()
    cursor = conn.cursor()
    query = """
      INSERT INTO publicaciones (id, titulo, categoria, descripcion, id_usuario, link) 
      VALUES (%s, %s, %s, %s, %s, %s)
    """

    link = ''
    # *Si existe algun link a una red social, se agrega, de lo contrario queda vacio
    if data.get('link'):
      link = data.get('link')

    values = (
      getId(),
      data.get('title'),
      data.get('category'),
      data.get('content'),
      data.get('id_user'),
      link
    )
    cursor.execute(query, values)
    conn.commit()
    conn.close()

    return True
  except Exception as e:
    print("Error al crear el post: ",e)
    return False
  
def editPost(data):
  try:
    conn = initConn()
    cursor = conn.cursor()
    query = """
      UPDATE publicaciones 
      SET titulo=%s, categoria=%s, descripcion=%s, link=%s, last_mod=NOW()
      WHERE id=%s AND eliminado=false
    """
    values = (
      data.get('title'),
      data.get('category'),
      data.get('content'),
      data.get('link'),
      data.get('id')
    )
    cursor.execute(query, values)
    conn.commit()
    conn.close()

    return True
  except Exception as e:
    print("Error al editar el post: ",e)
    return False
  
def deletePost(id):
  try:
    conn = initConn()
    cursor = conn.cursor()
    query = """
      UPDATE publicaciones SET eliminado=true, last_mod=NOW() WHERE id=%s AND eliminado=false
    """
    cursor.execute(query, (id,))
    conn.commit()
    conn.close()

    return True
  except Exception as e:
    print("Error al eliminar el post: ",e)
    return False
  
def increaseInteresados(id):
  try:
    conn = initConn()
    cursor = conn.cursor()
    query = """
      UPDATE publicaciones SET interesados=interesados+1 WHERE id=%s AND eliminado=false
    """
    cursor.execute(query, (id,))
    conn.commit()
    conn.close()

    return True
  except Exception as e:
    print("Error al aumentar los interesados: ",e)
    return False