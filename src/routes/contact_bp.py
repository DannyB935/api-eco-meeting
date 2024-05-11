from models.contact import *
from flask import Blueprint, request, jsonify

contact_bp = Blueprint('contact_bp', __name__)

@contact_bp.route('/get-messages', methods=['GET'])
def getMessagesRoute():
  try:
    messages = getMensajes()
    if messages:
      return jsonify({'status': 'success', 'messages': messages})
    return jsonify({'status': 'ok', 'message': 'No hay mensajes de contacto para mostrar'})
  except Exception as e:
    print("Error al obtener todos los mensajes /get-messages ",e)
    return jsonify({'status': 'error', "message": "Error al obtener todos los mensajes"})
  
@contact_bp.route('/get-message/<string:id>', methods=['GET'])
def getMessageRoute(id):
  try:
    message = getMensaje(id)
    if message:
      return jsonify({'status': 'success', 'message': message})
    return jsonify({'status': 'ok', 'message': f'No existe el mensaje con id {id}'})
  except Exception as e:
    print("Error al obtener el mensaje /get-message ",e)
    return jsonify({'status': 'error', "message": "Error al obtener el mensaje"})
  
@contact_bp.route('/create-message', methods=['POST'])
def createMessageRoute():
  if request.method == 'POST':
    try:
      data = request.form
      # *Si hay spam de mensajes, primero lo comprueba y envia la respuesta
      if checkSpam(data):
        return jsonify({'status': 'ok', 'message': 'No puedes enviar mas de 3 mensajes en menos de 5 minutos'})
      if createMensaje(data):
        return jsonify({'status': 'success', 'message': 'Mensaje enviado correctamente'})
      return jsonify({'status': 'ok', 'message': 'Error al enviar el mensaje'})
    except Exception as e:
      print("Error al crear el mensaje /create-message ",e)
      return jsonify({'status': 'error', "message": "Error al crear el mensaje"})
    
  return jsonify({'status': 'ok', 'message': 'Metodo no permitido'})

@contact_bp.route('/delete-message', methods=['POST'])
def deleteMessageRoute():
  if request.method == 'POST':
    try:
      data = request.form
      if deleteMensaje(data.get('id')):
        return jsonify({'status': 'success', 'message': 'Mensaje eliminado correctamente'})
      return jsonify({'status': 'ok', 'message': 'Error al eliminar el mensaje'})
    except Exception as e:
      print("Error al eliminar el mensaje /delete-message ",e)
      return jsonify({'status': 'error', "message": "Error al eliminar el mensaje"})
    
  return jsonify({'status': 'ok', 'message': 'Metodo no permitido'})