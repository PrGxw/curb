from urllib.request import urlopen
import json
from rps.model.GameItem import GameItem

class Game:
    def __init__(self):
        self.user_choice = None
        self.curb_choice = None
        production = 'https://5eddt4q9dk.execute-api.us-east-1.amazonaws.com/rps-stage/throw'
        mockserver = 'https://private-anon-5726016a19-curbrockpaperscissors.apiary-mock.com/rps-stage/throw'
        debug = "https://5eddt4q9dk.execute-api.us-east-1.amazonaws.com/rps-stage/throw"
        self.API_URL = debug

    def get_curb_choice(self):
        html = urlopen(self.API_URL).read()
        response = json.loads(html)
        if (response.get("statusCode", 0) == 200):
            self.set_curb_choice(response["body"]) if(response.get("body")) else self.set_curb_choice(None)
        else:
            self.set_curb_choice(None)
        return self.curb_choice

    def get_user_choice(self):
        return self.user_choice

    def set_user_choice(self, choice):
        self.user_choice = GameItem.convert(choice)

    def set_curb_choice(self, choice):
        self.curb_choice = GameItem.convert(choice)

    def determine_winner(self):
        return GameItem.determine_winner(self.curb_choice, self.user_choice)

