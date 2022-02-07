from pickle import GET
from flask import Flask

app = Flask(__name__)

@app.route("/olamundo", methods=["GET"])
def olaMundo():
    return {"ola": "mundo" }

app.run()