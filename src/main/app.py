from db_create import db_create
from flask import Flask, jsonify
from db_queries import query_by_name, query_by_number, query_moves_by_type, query_pokemon_by_type
from flask_cors import CORS

app = Flask(__name__)
app.json.sort_keys = False
#when using Flask-Cors The core best practice is to strictly avoid the 
# wildcard (*) in production and restrict allowed origins, paths, 
# and methods. We will lock it down to only accepting from the localhost 
#frontend files.
CORS(app, origins=["http://localhost:5173/"])

#To run this file you will need to use the virtual enviornment and make sure
#the correct dependencies are installed (ex. flask) 
#Make sure to ACTIVATE THE VENV! 
# .\.venv\Scripts\Activate.ps1
#Use the commands below:
# python -m pip install flask flask-cors
# python -m pip show flask
# Then run the file
#from the terminal (powershell) using "python .\src\main\app.py"


@app.route("/")
def home():
    return """<pre>Welcome to the Pokedex API Project

Currently Supported Endpoints

pokemon_by_name

pokemon_by_number

pokemon_by_type

moves_by_type</pre>"""

@app.route("/pokemon_by_name/<name>")
def show_pokemonInfoByName(name):
    cursor = db_create()
    try:
        return jsonify(query_by_name(cursor, name))
    finally:
        cursor.close()

@app.route("/pokemon_by_number/<number>")
def show_pokemonInfoByNumber(number):
    cursor = db_create()
    try:
        return jsonify(query_by_number(cursor, number))
    finally:
        cursor.close()

@app.route("/moves_by_type/<type>")
def show_movesByType(type):
    cursor = db_create()
    try:
        return jsonify(query_moves_by_type(cursor, type))
    finally:
        cursor.close()

@app.route("/pokemon_by_type/<type>")
def show_pokemonByType(type):
    cursor = db_create()
    try:
        return jsonify(query_pokemon_by_type(cursor, type))
    finally:
        cursor.close()


if __name__ == "__main__":
    app.run(debug=True)