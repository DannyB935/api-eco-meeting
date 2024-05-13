from flask import Blueprint, jsonify, request
from ..models.usuarios import *

usuariosBp = Blueprint('usuariosBp', __name__)

@usuariosBp.route('/usuarios', methods=['GET'])
def getUsuariosRoute():
  try:
    usuarios = getUsuarios()
    if usuarios:
      return jsonify({'status': 'success', 'usuarios': usuarios}), 200
    return jsonify({'status': 'ok', 'message': 'No hay usuarios'}), 200
  except Exception as e:
    return jsonify({'status': 'error', 'message': 'Error al obtener los usuarios'}), 500
  
@usuariosBp.route('/nuevo-usuario', methods=['POST'])
def registerRoute():
  if request.method == 'POST':
    try:
      data = request.form
      if registrarUsuario(data):
        return jsonify({'status': 'success', 'message': 'Usuario registrado'}), 200
      return jsonify({'status': 'ok', 'message': 'El usuario no se pudo registrar'}), 200
    except Exception as e:
      return jsonify({'status': 'error', 'message': 'Ocurrio un error al registrar al usuario'}), 500
  return jsonify({'status': 'ok', 'message': 'Error al registrar el usuario'}), 500

@usuariosBp.route('/login', methods=['POST'])
def loginRoute():
  if request.method == 'POST':
    try:
      data = request.form
      usuario = loginUsuario(data.get('user_name'), data.get('password'))
      if usuario:
        return jsonify({'status': 'success', 'message': 'Inicio de sesión correcto', 'user': usuario}), 200
      return jsonify({'status': 'ok', 'message': 'El nombre de usuario o contrasenia son incorrectos'}), 200
    except Exception as e:
      print("Error al iniciar sesión /login: ",e)
      return jsonify({'status': 'error', 'message': 'Error al iniciar sesión'}), 500
    
@usuariosBp.route('/get-user', methods=['POST'])
def getUserRoute():
  if request.method == 'POST':
    try:
      data = request.form
      usuario = getUsuario(data.get('id'))
      if usuario:
        return jsonify({'status': 'success', 'message': 'Usuario encontrado', 'user': usuario}), 200
      return jsonify({'status': 'ok', 'message': 'Usuario no encontrado'}), 200
    except Exception as e:
      print("Error al obtener el usuario /get-user: ",e)
      return jsonify({'status': 'error', 'message': 'Error al obtener el usuario'}), 500