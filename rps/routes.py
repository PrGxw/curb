from rps import app
from flask import render_template, jsonify, request
from rps.model.GameItem import GameItem


from rps.model.Game import Game
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

    return render_template('index.html')


@app.route('/game', methods=["POST"])
def game():
    g = Game()
    userChoice = request.form['userChoice'] if (request.form.get("userChoice")) else GameItem.UNDEFINED
    g.set_user_choice(userChoice)
    curbChoice = g.get_curb_choice()

    return jsonify({"curbChoice": str(curbChoice), "result": str(g.determine_winner())})