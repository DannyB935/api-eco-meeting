from flask import Blueprint, jsonify, request
from ..models.tips import *

tipsBp = Blueprint('tipsBp', __name__)

@tipsBp.route('/tips', methods=['GET'])
def getTipsRoute():
  try:
    tips = getTips()
    if tips:
      return jsonify({'status': 'success', 'tips': tips}), 200
    return jsonify({'status': 'ok', 'message': 'No hay tips'}), 200
  except Exception as e:
    return jsonify({'status': 'error', 'message': 'Error al obtener los tips'}), 500
  
@tipsBp.route('/user-tips', methods=['POST'])
def getUserTipsRoute():
  if request.method == 'POST':
    try:
      data = request.form
      tips = getUserTips(data.get('id'))
      if tips:
        return jsonify({'status': 'success', 'tips': tips}), 200
      return jsonify({'status': 'ok', 'message': 'No hay tips para este usuario'}), 200
    except Exception as e:
      print("Error al obtener los tips del usuario: ",e)
      return jsonify({'status': 'error', 'message': 'Error al obtener los tips del usuario'}), 500
    
@tipsBp.route('/tip/<string:id>', methods=['GET'])
def getTipRoute(id):
  try:
    tip = getTip(id)
    if tip:
      return jsonify({'status': 'success', 'tip': tip}), 200
    return jsonify({'status': 'ok', 'message': 'No hay tip'}), 200
  except Exception as e:
    return jsonify({'status': 'error', 'message': 'Error al obtener el tip'}), 500

@tipsBp.route('/create-tip', methods=['POST'])
def createTipRoute():
  if request.method == 'POST':
    try:
      data = request.form
      if createTip(data):
        return jsonify({'status': 'success', 'message': 'Tip creado correctamente'}), 200
      return jsonify({'status': 'ok', 'message': 'Error al crear el tip'}), 200
    except Exception as e:
      return jsonify({'status': 'error', 'message': 'Error al crear el tip'}), 500
    
@tipsBp.route('/edit-tip', methods=['POST'])
def editTipRoute():
  if request.method == 'POST':
    try:
      data = request.form
      if editTip(data):
        return jsonify({'status': 'success', 'message': 'Tip editado correctamente'}), 200
      return jsonify({'status': 'ok', 'message': 'Error al editar el tip'}), 200
    except Exception as e:
      return jsonify({'status': 'error', 'message': 'Error al editar el tip'}), 500

@tipsBp.route('/delete-tip', methods=['POST'])
def deleteTipRoute():
  if request.method == 'POST':
    try:
      data = request.form
      if deleteTip(data.get('id'), data.get('id_user')):
        return jsonify({'status': 'success', 'message': 'Tip eliminado correctamente'}), 200
      return jsonify({'status': 'ok', 'message': 'Error al eliminar el tip'}), 200
    except Exception as e:
      return jsonify({'status': 'error', 'message': 'Error al eliminar el tip'}), 500
    
@tipsBp.route('/like-tip/<string:id>', methods=['GET'])
def likeTipRoute(id):
  try:
    if likeTip(id):
      return jsonify({'status': 'success', 'message': 'Like dado correctamente'}), 200
    return jsonify({'status': 'ok', 'message': 'Error al dar like al tip'}), 200
  except Exception as e:
    return jsonify({'status': 'error', 'message': 'Error al dar like al tip'}), 500

@tipsBp.route('/dislike-tip/<string:id>', methods=['GET'])
def dislikeTipRoute(id):
  try:
    if dislikeTip(id):
      return jsonify({'status': 'success', 'message': 'Dislike dado correctamente'}), 200
    return jsonify({'status': 'ok', 'message': 'Error al dar dislike al tip'}), 200
  except Exception as e:
    return jsonify({'status': 'error', 'message': 'Error al dar dislike al tip'}), 500
  
@tipsBp.route('/report-tip/<string:id>', methods=['GET'])
def reportTipRoute(id):
  try:
    if reportarTip(id):
      return jsonify({'status': 'success', 'message': 'Reporte enviado correctamente'}), 200
    return jsonify({'status': 'ok', 'message': 'Error al reportar el tip'}), 200
  except Exception as e:
    return jsonify({'status': 'error', 'message': 'Error al reportar el tip'}), 500