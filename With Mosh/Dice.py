import random


class Dice:
    def roll(self):
        output = (random.randint(1, 6), random.randint(1, 6))
        return output
