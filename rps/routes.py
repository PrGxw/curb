from rps import app
from flask import render_template, flash, jsonify, request
from rps.forms import RPSForm
import json
from rps.model.GameItem import GameItem
from rps.model.Game import Game
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    # form = RPSForm()
    # if form.validate_on_submit():
    #     print('rock') if form.rock.data else (print("paper") if (form.paper.data) else print('scissor'))
    #
    #     flash(
    #         "You submitted via button {button}".format(
    #             button="rock" if form.rock.data else ("paper" if (form.paper.data) else 'scissor')
    #         )
    #     )
    #     return jsonify()
    return render_template('index.html')


@app.route('/game', methods=["POST"])
def game():
    g = Game()
    userChoice = request.form['userChoice']
    g.set_user_choice(userChoice)
    curbChoice = g.get_curb_choice()

    return jsonify({"curbChoice": str(curbChoice), "result": str(g.determine_winner())})