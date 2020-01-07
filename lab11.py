import numpy as np
import random

# -------------------------------------------------
# CSCI 127, Lab 11
# November 14, 2017
# Tyler Bourgeois
# -------------------------------------------------

class Die:

    def __init__(self, sides):
        """A constructor method to create a die"""
        self.sides = sides

    def roll(self):
        """A general method to roll the die"""
        return random.randint(1, self.sides)

# -------------------------------------------------

class Yahtzee:

    def __init__(self):
        """A constructor method that can record 5 dice rolls"""
        self.rolls = np.zeros(5, dtype=np.int16)

    def roll_dice(self):
        """A general method that rolls 5 dice"""
        for i in range(len(self.rolls)):
            self.rolls[i] = Die(6).roll()

    def count_outcomes(self):
        """A helper method that determines how many 1s, 2s, etc. were rolled"""
        counts = np.zeros(7, dtype=np.int16)
        for roll in self.rolls:
            counts[roll] += 1
        return counts

    def is_it_yahtzee(self):
        if(np.all(self.rolls == self.rolls[0])):
            return True

    def is_it_full_house(self):
        r = np.sort(self.rolls)
        if(((r[0] == r[1]) and (r[2] == r[3] == r[4])) or ((r[0] == r[1] == r[2]) and (r[3] == r[4]))):
            return True
            

    def is_it_large_straight(self):
        new_rolls = np.sort(self.rolls)
        if(new_rolls[1] == (new_rolls[0] + 1) and new_rolls[2] == (new_rolls[1] + 1) and new_rolls[3] == (new_rolls[2] + 1) and new_rolls[4] == (new_rolls[3] + 1)):
            return True


# -------------------------------------------------
        
def main(how_many):

    yahtzees = 0
    full_houses = 0
    large_straights = 0
    game = Yahtzee()

    for i in range(how_many):
        game.roll_dice()
        if game.is_it_yahtzee():
            yahtzees += 1
        elif game.is_it_full_house():
            full_houses += 1
        elif game.is_it_large_straight():
            large_straights += 1

    print("Number of Rolls:", how_many)
    print("---------------------")
    print("Number of Yahtzees:", yahtzees)
    print("Yahtzee Percent:", "{:.2f}%\n".format(yahtzees * 100 / how_many))
    print("Number of Full Houses:", full_houses)
    print("Full House Percent:", "{:.2f}%\n".format(full_houses * 100 / how_many))
    print("Number of Large Straights:", large_straights)
    print("Large Straight Percent:", "{:.2f}%".format(large_straights * 100 / how_many))

# -------------------------------------------------

main(5000)
    
        
