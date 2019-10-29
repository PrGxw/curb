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
    game_instance = Game()
    user_choice = request.form['userChoice'] if (request.form.get("userChoice")) else None
    game_instance.set_user_choice(user_choice)
    curb_choice = game_instance.get_curb_choice()

    return jsonify({"curbChoice": str(curb_choice), "result": str(game_instance.determine_winner())})
