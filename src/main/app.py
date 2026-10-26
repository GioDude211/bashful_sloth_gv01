from db_create import db_create
from flask import Flask, jsonify
from db_queries import query_by_name, query_by_number, query_moves_by_type, query_pokemon_by_type

app = Flask(__name__)

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
        return query_pokemon_by_type(cursor, type)
    finally:
        cursor.close()


if __name__ == "__main__":
    app.run(debug=True)