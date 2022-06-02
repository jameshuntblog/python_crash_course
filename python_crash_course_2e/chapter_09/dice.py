# dice.py

from random import randint

class Die:
    def __init__(self,sides,rolls):
        self.sides = sides
        self.rolls = rolls

    def roll_die(self):
        for roll in range(self.rolls):
            print(randint(1,self.sides))

six_sided_die_rolling_10_times = Die(6,10)
six_sided_die_rolling_10_times.roll_die()

ten_sided_die_rolling_10_times = Die(10,10)
ten_sided_die_rolling_10_times.roll_die()

twenty_sided_die_rolling_10_times = Die(20,10)
twenty_sided_die_rolling_10_times.roll_die()