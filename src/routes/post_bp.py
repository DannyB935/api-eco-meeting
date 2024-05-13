from flask import Blueprint, jsonify, request
from ..models.post import *

postBp = Blueprint('postBp', __name__)

@postBp.route('/posts', methods=['GET'])
def getPostsRoute():
  try:
    posts = getPosts()
    if posts:
      return jsonify({'status': 'success', 'posts': posts}), 200
    return jsonify({'status': 'ok', 'message': 'No hay posts'}), 200
  except Exception as e:
    print("Error al obtener los posts /posts: ",e)
    return jsonify({'status': 'error', 'message': 'Error al obtener los posts'}), 500
  
@postBp.route('/post/<string:id>', methods=['GET'])
def getPostRoute(id):
  try:
    post = getPost(id)
    if post:
      return jsonify({'status': 'success', 'post': post}), 200
    return jsonify({'status': 'ok', 'message': 'No hay post'}), 200
  except Exception as e:
    print(f"Error al obtener el post con el id: {id} /post/id: {e}")
    return jsonify({'status': 'error', 'message': 'Error al obtener el post'}), 500
  
@postBp.route('/user-posts', methods=['POST'])
def getUserPostsRoute():
  if request.method == 'POST':
    try:
      data = request.form
      id = data.get('id_user')
      posts = getUserPost(id)
      if posts:
        return jsonify({'status': 'success', 'posts': posts}), 200
      return jsonify({'status': 'ok', 'message': 'No hay posts'}), 200
    except Exception as e:
      print(f"Error al obtener los posts de un usuario con el id: {id} /user-posts: {e}")
      return jsonify({'status': 'error', 'message': 'Error al obtener los posts de un usuario'}), 500
    
  return jsonify({'status': 'error', 'message': 'Metodo no permitido'}), 405

@postBp.route('/new-post', methods=['POST'])
def createPostRoute():
  if request.method == 'POST':
    try:
      data = request.form
      if createPost(data):
        return jsonify({'status': 'success', 'message': 'Post creado'}), 200
      return jsonify({'status': 'ok', 'message': 'No se pudo crear el post'}), 200
    except Exception as e:
      print(f"Error al crear un post /new-post: {e}")
      return jsonify({'status': 'error', 'message': 'Error al crear el post'}), 500
    
  return jsonify({'status': 'error', 'message': 'Metodo no permitido'}), 405

@postBp.route('/edit-post', methods=['POST'])
def editPostRoute():
  if request.method == 'POST':
    try:
      data = request.form
      if editPost(data):
        return jsonify({'status': 'success', 'message': 'Post editado'}), 200
      return jsonify({'status': 'ok', 'message': 'No se pudo editar el post'}), 200
    except Exception as e:
      print(f"Error al editar un post /edit-post: {e}")
      return jsonify({'status': 'error', 'message': 'Error al editar el post'}), 500
    
  return jsonify({'status': 'error', 'message': 'Metodo no permitido'}), 405

@postBp.route('/delete-post', methods=['POST'])
def deletePostRoute():
  if request.method == 'POST':
    try:
      data = request.form
      if deletePost(data.get('id')):
        return jsonify({'status': 'success', 'message': 'Post eliminado'}), 200
      return jsonify({'status': 'ok', 'message': 'No se pudo eliminar el post'}), 200
    except Exception as e:
      print(f"Error al eliminar un post /delete-post: {e}")
      return jsonify({'status': 'error', 'message': 'Error al eliminar el post'}), 500
    
  return jsonify({'status': 'error', 'message': 'Metodo no permitido'}), 405

@postBp.route('/interes-post', methods=['POST'])
def interestPostRoute():
  if request.method == 'POST':
    try:
      data = request.form
      if increaseInteresados(data.get('id')):
        return jsonify({'status': 'success', 'message': 'Agregado un interesado mas al post'}), 200
      return jsonify({'status': 'ok', 'message': 'No se pudo marcar como interesado el post'}), 200
    except Exception as e:
      print(f"Error al marcar como interesado un post /interes-post: {e}")
      return jsonify({'status': 'error', 'message': 'Error al marcar como interesado el post'}), 500
    
  return jsonify({'status': 'error', 'message': 'Metodo no permitido'}), 405