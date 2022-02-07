from pickle import GET
from flask import Flask, request, jsonify
from pyparsing import java_style_comment
from into import insertDados

app = Flask(__name__)

age = 1
education_level = ["no_education", "high_school", "bachelors_degree_or_high"]

{
  "age": 35,
  "education_level": "high_school"
   }


@app.route("/dados", methods=["GET"])
def olaMundo():
    return {"ola": "mundo"}

@app.route('/date')
def get_current_date():
	favorite_pizza = {
		"John": "Pepperoni",
		"Mary": "Cheese"
	}
	return favorite_pizza



#@app.route("/cadastra/usuario", methods=["POST"])
#def cadastrarUsuario():
#    body = request.get_json()
#    usuario = insertDados(body["age"], body["education_level"])#(body["age"], body["education_level"], body["sales"], body["support"], body["download_speed"], body["upload_speed"], body["writing_score"])
#    return usuario

#age, education_level, sales, support, download_speed, upload_speed,  writing_score

app.run()