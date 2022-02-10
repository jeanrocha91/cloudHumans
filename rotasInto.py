import json
import os
from crypt import methods
from pickle import GET
from flask import Flask, request, jsonify
from pyparsing import java_style_comment
from into import insertDados

app = Flask(__name__)

age = 1
education_level = ["no_education", "high_school", "bachelors_degree_or_high"]
past_experiences = {
    "sales": False,
    "support": True
   }
internet_test = {
    "download_speed": 50.4,
    "upload_speed": 40.2
  }
writing_score = 0
referral_code = "token1234"

favorite_pizza = {
		"John": "Pepperoni",
		"Mary": "Cheese"
	}

data = [
    {
        "age": 35,
        "education_level": "high_school",
       
        "past_experiences": {
            "sales": False,
            "support": True,
        },
        "internet_test": {
            "download_speed": 50.4,
            "upload_speed": 40.2,
        },
        "writing_score": 0.6,
        "referral_code": "token1234",
    },
]

@app.route('/dados', methods=["GET"])
def olaMundo():
    return {"ola": "mundo"}

@app.route('/pizza')
def get_current_date():
	return favorite_pizza

@app.route('/data')
def return_data():
	return jsonify(data)

#@app.route('/data-details', methods=["GET"])
#def find_data():
#    datails = {
#    "score": 7,
#    "selected_project": "determine_schrodinger_cat_is_alive",
#    "eligible_projects": ["determine_schrodinger_cat_is_alive", "support_users_from_xyz", "collect_information_for_xpto"],
#    "ineligible_projects": ["calculate_dark_matter_nasa"]
#    }
#    return details

#@app.route("/cadastra/usuario", methods=["POST"])
#def cadastrarUsuario():
#    body = request.get_json()
#    usuario = insertDados(body["age"], body["education_level"])#(body["age"], body["education_level"], body["sales"], body["support"], body["download_speed"], body["upload_speed"], body["writing_score"])
#    return usuario

#age, education_level, sales, support, download_speed, upload_speed,  writing_score

BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'arquivo-data.json')

with open(SAVE_TO, 'w') as file:
    json.dump(data, file, indent=2)

app.run()