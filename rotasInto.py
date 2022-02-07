from pickle import GET
from flask import Flask, request, jsonify
from pyparsing import java_style_comment
from into import insertDados

app = Flask(__name__)

@app.route("/dados", methods=["GET"])
def olaMundo():
    return jsonify(insertDados), 200

#@app.route("/cadastra/usuario", methods=["POST"])
#def cadastrarUsuario():
#    body = request.get_json()
#    usuario = insertDados(body["age"], body["education_level"])#(body["age"], body["education_level"], body["sales"], body["support"], body["download_speed"], body["upload_speed"], body["writing_score"])
#    return usuario

#age, education_level, sales, support, download_speed, upload_speed,  writing_score

app.run()