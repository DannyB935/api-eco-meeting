from flask import Blueprint, jsonify, request
from models.usuarios import *

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