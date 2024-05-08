import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def initConn():
  try:
    conn = mysql.connector.connect(
      host=os.getenv('DB_HOST'),
      user=os.getenv('DB_USER'),
      password=os.getenv('DB_PASSWORD'),
      database=os.getenv('DB_NAME'),
      port=os.getenv('DB_PORT')
    )

    return conn
  except mysql.connector.Error as e:
    print("Error al conectar a la base de datos: ",e)
    return None