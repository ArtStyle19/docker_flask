from flask import Flask, request, jsonify, Response
import json
import mysql.connector
from flask_cors import CORS, cross_origin

app = Flask(__name__)

def getMysqlConnection():
    return mysql.connector.connect(user='root', host='0.0.0.0', port='3306', password='41818', database='my_db', auth_plugin='mysql_native_password')

@app.route("/")
def hello():
    return "Flask inside Docker!!"

db = getMysqlConnection()
cursor = db.cursor() # Crear un cursor para interactuar con la base de datos
# @app.route('/api/', methods=['GET'])
# @cross_origin() # allow all origins all methods.
# def get_months():
#     db = getMysqlConnection()
#     print(db)
#     try:
#         sqlstr = "SELECT * from test_table"
#         print(sqlstr)
#         cur = db.cursor()
#         cur.execute(sqlstr)
#         output_json = cur.fetchall()
#     except Exception as e:
#         print("Error in SQL:\n", e)
#     finally:
#         db.close()
#     return jsonify(results=output_json)

@app.route('/data', methods=['GET'])

def get_data():
    cursor.execute("SELECT * FROM test_table") # Ejecutar una consulta SQL
    result = cursor.fetchall() # Obtener todos los resultados de la consulta
    return jsonify(result) # Devolver los resultados en formato JSON 

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
