""" Craps Game Programming Example 

This module was created to provide an example of the basic Python concepts
such as:

    * variables
    * lists
    * dictionaries
    * classes
    * methods
    * modules
    * ASCII art / animation

This is a simple version of CRAPS, the casion dice game. The rules were included in
the class documentation.

Date : December 27, 2021
Author : Princton C. Brennan

"""

import random
import os
import time


class Die:
    """
    A single die with 6 sides to be rolled during a game.
    """

    current_side = None
    side_values = [1, 2, 3, 4, 5, 6]

    def __init__(self):
        """
        Initializes Die object w/ an initial roll.
        """
        self.roll_die

    def roll_die(self):
        """
        Simulates the rolling of a die to generate, and returns the current value that
        the die has landed on. 
        """
        self.current_side = random.choice(self.side_values)
        return self.current_side


class Roll_Combo:
    """
    Two die roll combination for games that require dice to play.
    """

    sum : int
    is_doubles : bool 

    def __init__(self, val1: int, val2 : int = None):
        """
        Intializes Roll Combo object by summing 

        @param val1 : value of the first die's currently rolled value
        @param val2 : value of the first die's currently rolled value
        """
        if val2 is None:
            self.is_doubles = False
            self.sum = val1
        else:
            self.sum = val1 + val2
            self.is_doubles = (val1 == val2)

    @property
    def properties(self):
        """
        Returns the sum of the roll as well as if it was a doubles.

        :return _properties : calculated values for dice roll 
        :rtype dict
        """
        _properties = self.__dict__
        return _properties


class Craps:
    """
    Craps game to play as a single player.

    Rules: Player places a bet of $1, $5, or $10. On the first roll
    if the player rolls a 7 or 11, the player automaticalaly wins. If
    the player rolls a 2, 3, or a 12 on the first roll, that is an 
    automatic loss.
    
    If the player rolls a 4, 5, 6, 8, 9, or 10, that is the 'Set Point',
    and the player must roll until that same number is thrown. However,
    if the player rolls a 7 at this point, that is now a loss.
    
    """

    DICE_ART = "".join(open("dice_art.txt", 'r').readlines())
    DICE_ANIMATIONS = [
        "".join(open("dice_animation_0.txt", 'r').readlines()), 
        "".join(open("dice_animation_1.txt", 'r').readlines())
        ]
    
    RULES = """
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
    Rules: Player places a bet of $1, $5, or $10. On the first roll
    if the player rolls a 7 or 11, the player automaticalaly wins. If
    the player rolls a 2, 3, or a 12 on the first roll, that is an 
    automatic loss.

    If the player rolls a 4, 5, 6, 8, 9, or 10, that is the 'Set Point',
    and the player must roll until that same number is thrown. However,
    if the player rolls a 7 at this point, that is now a loss.
    -*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
    """

    user_selection = None
    set_point = None 
    user_wallet = 0
    bet = 0
    dice: list[Die]
    die_1 = Die()
    die_2 = Die()

    ROLLS = {
        "Snake Eyes" : Roll_Combo(1,1).properties,
        "Hard Four" : Roll_Combo(2, 2).properties,
        "Hard Six" : Roll_Combo(3, 3).properties,
        "Hard Eight" : Roll_Combo(4, 4).properties,
        "Hard Ten" : Roll_Combo(5, 5).properties,
        "Boxcars / Midnight" : Roll_Combo(6, 6).properties,
        "Ace Deuce" : Roll_Combo(3).properties,
        "Easy Four" : Roll_Combo(4).properties,
        "Five" : Roll_Combo(5).properties,
        "Easy Six" : Roll_Combo(6).properties,
        "Natural / Seven Out" : Roll_Combo(7).properties,
        "Easy Eight" : Roll_Combo(8).properties,
        "Nina" : Roll_Combo(9).properties,
        "Easy Ten" : Roll_Combo(10).properties,
        "Yo / Yo-leven" : Roll_Combo(11).properties
    }

    def __init__(self):
        """
        Initializes the Craps object as an instance of a CRAPS game.
        """
        self.user_selection = input("Welcome to Craps!\nWould you like to play?\n\t(Y) yes or (N) no\n\t")
        if self.user_selection.upper() == "YES" or self.user_selection.upper() == "Y":
            self.set_point = None
            dice = [self.die_1, self.die_2]
            os.system("clear")
            print("\nWelcome!")
            print(self.DICE_ART)
            
            self.user_selection = input("Type 'R' to roll, or any other key to quit.\nOr 'H' for help with how to play.\n\t")
            while self.user_selection is None or self.user_selection.upper() == "R" or self.user_selection.upper() == "H":
                if self.user_selection.upper() == "R":
                    for die in dice:
                        die.roll_die()
                    
                    self.animate_dice()
                    print(self.DICE_ANIMATIONS[-1] + "\n")
                    print("Die 1: " + str(self.die_1.current_side) + ", Die 2: " + str(self.die_2.current_side))

                    roll_combo = Roll_Combo(dice[0].current_side,dice[1].current_side)
                    self.check_roll(roll_combo)

                    self.user_selection = input("Type 'R' to roll, or any other key to quit.\n\t")
                else:
                    os.system("clear")
                    print(self.RULES)
                    self.user_selection = input("Type 'R' to roll, or any other key to quit.\nOr 'H' for help with how to play.\n\t")
            
            print("\nThank you for playing!\n")
        else:
            print("\nOK, see you next time.")

    def check_roll(self, roll_combo: Roll_Combo):
        """
        Evaluates the recent roll's value and confirms if the user loses, wis, or continues.

        @param roll_combo: The recent user's simulated roll result.
        @type roll_combo: Roll_Combo
        """

        roll = list(self.ROLLS.keys())[list(self.ROLLS.values()).index(roll_combo.properties)]
        print("\n~~~~~ " + roll + " ~~~~~\n")
        if self.set_point is None:
            if roll_combo.sum == 7 or roll_combo.sum == 11:
                print("YOU WIN!\n")
            elif roll_combo.sum == 2 or roll_combo.sum == 3 or roll_combo.sum == 12:
                print("SORRY! YOU LOSE!\n")
            else:
                print("SET POINT : {0}!".format(roll_combo.sum))
                self.set_point = roll_combo.sum
        else:
            if roll_combo.sum == self.set_point:
                print("YOU WIN!\n")
                self.set_point = None
            elif roll_combo.sum == 7:
                print("SORRY! YOU LOSE\n")
                self.set_point = None
            else:
                print("TRY AGAIN! SET POINT STILL {0}!\n".format(self.set_point))

    def animate_dice(self):
        """
        Runs through simple dice ASCII art animation.
        """
        os.system("clear")
        loop_limit = 3
        for i in range(0, loop_limit):
            for dice_animation in self.DICE_ANIMATIONS:
                print(dice_animation)
                time.sleep(1)
                os.system("clear")


if __name__ == "__main__":
    game = Craps()