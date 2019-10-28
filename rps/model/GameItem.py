from enum import Enum



class GameItem(Enum):
    ROCK = 'rock'
    PAPER   = 'paper'
    SCISSOR = 'scissor'
    UNDEFINED = 'undefined'


    @classmethod
    def convert(cls, s):
        s = s.lower().strip(" ")
        if (s == str(cls.ROCK)):
            return cls.ROCK
        elif (s == str(cls.PAPER)):
            return cls.PAPER
        elif (s == str(cls.SCISSOR)):
            return cls.SCISSOR
        else:
            return cls.UNDEFINED

    def __str__(self):
        return str(self.value)