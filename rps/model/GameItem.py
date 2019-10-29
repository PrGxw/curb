from enum import Enum
import re

class GameItem(Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSOR = "scissor"

    @classmethod
    def convert(cls, s):
        if (s == None):
            return None

        s = re.sub("[^a-z]*", "", s.lower())

        if (s in [str(cls.ROCK), str(cls.PAPER), str(cls.SCISSOR)] ):
            return GameItem(s)
        if s == "scissors":
            return cls.SCISSOR
        return None

    @staticmethod
    def determine_winner(curb_choice, user_choice):
        if (curb_choice == None) or (user_choice == None):
            return "UNDEFINED"
        if (user_choice == curb_choice):
            return "TIE"
        if curb_choice < user_choice:
            return "YOU WIN"
        return "YOU LOST"

    def __str__(self):
        return "{0}".format(self.value)

    def __lt__(self, other):
        if self == GameItem.ROCK and other == GameItem.SCISSOR:
            return False
        return len(str(self)) > len(str(other))
