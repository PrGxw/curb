from urllib.request import urlopen
import json
from rps.model.GameItem import GameItem

class Game:
    def __init__(self):
        self.user_choice = None
        self.curb_choice = None
        self.API_URL = "https://private-anon-ccd7a57b7f-curbrockpaperscissors.apiary-mock.com/rps-stage/throw"

    def get_curb_choice(self):
        # html = urlopen(self.API_URL).read()
        # response = json.loads(html)
        # if (response["statusCode"] == 200):
        #     self.set_curb_choice(response["body"])
        # # self.set_curb_choice(GameItem.ROCK)
        # return self.curb_choice

        html = urlopen(self.API_URL).read()
        response = json.loads(html)
        while (response["statusCode"] == 200):
            self.set_curb_choice(response["body"])
        # self.set_curb_choice(GameItem.ROCK)
        return self.curb_choice

    def get_user_choice(self):
        return self.user_choice

    def set_user_choice(self, choice):
        self.user_choice = GameItem.convert(choice)

    def set_curb_choice(self, choice):
        self.curb_choice = GameItem.convert(choice)

    def determine_winner(self):
        print(self.user_choice, self.curb_choice)
        if (self.user_choice == GameItem.UNDEFINED) or (self.curb_choice == GameItem.UNDEFINED):
            return "UNDEFINED"

        if (self.user_choice == self.curb_choice):
            result = "TIE"
        elif self.user_choice == GameItem.ROCK:
            result = "YOU WIN" if (self.curb_choice != GameItem.PAPER) else "YOU LOST"
        elif self.user_choice == GameItem.PAPER:
            result = "YOU WIN" if (self.curb_choice != GameItem.SCISSOR) else "YOU LOST"
        else:
            result = "YOU WIN" if (self.curb_choice != GameItem.ROCK) else "YOU LOST"
        return result
