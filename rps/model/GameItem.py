from enum import Enum
import re
import string


class GameItem(Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSOR = "scissor"
    UNDEFINED = "undefined"
    @classmethod
    def convert(cls, s):
        if (s == None) : return cls.UNDEFINED

        s = re.sub("[^a-z]*", "", s.lower())

        if (s in [str(cls.ROCK), str(cls.PAPER), str(cls.SCISSOR)] ):
            return GameItem(s)
        if  s == "scissors":
            return cls.SCISSOR
        return cls.UNDEFINED

    def __str__(self):
        return "{0}".format(self.value)