from flask import Flask
from flask_cors import CORS, cross_origin

from routes.usuarios_bp import usuariosBp
from routes.tips_bp import tipsBp

app = Flask(__name__)
app.register_blueprint(usuariosBp)
app.register_blueprint(tipsBp)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def test():
  return "Ruta de prueba API"

if __name__ == '__main__':
  app.run(debug=True)
