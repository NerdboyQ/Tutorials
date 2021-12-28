import random

class Die:
    """
    A single die with 6 sides to be rolled during a game.
    """

    current_side = None
    side_values = [1, 2, 3, 4, 5, 6]

    def __init__(self):
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
        if val2 is None:
            self.is_doubles = False
            self.sum = val1
        else:
            self.sum = val1 + val2
            self.is_doubles = (val1 & val2)

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
    is_first_roll = True
    user_wallet = 0
    bet = 0
    dice = []
    die_1 = Die()
    die_2 = Die()

    ROLLS = {
        "Snake Eyes" : Roll_Combo(1,1),
        "Hard Four" : Roll_Combo(2, 2),
        "Hard Six" : Roll_Combo(3, 3),
        "Hard Eight" : Roll_Combo(4, 4),
        "Hard Ten" : Roll_Combo(5, 5),
        "Boxcars / Midnight" : Roll_Combo(6, 6),
        "Ace Deuce" : Roll_Combo(3),
        "Easy Four" : Roll_Combo(4),
        "Five" : Roll_Combo(5),
        "Easy Six" : Roll_Combo(6),
        "Natural / Seven Out" : Roll_Combo(7),
        "Easy Eight" : Roll_Combo(8),
        "Nina" : Roll_Combo(9),
        "Easy Ten" : Roll_Combo(10),
        "Yo / Yo-leven" : Roll_Combo(11)
    }

    def __init__(self):
        self.user_selection = input("Welcome to Craps!\nWould you like to play?\n\t(Y) yes or (N) no\n")
        if self.user_selection.upper() == "YES" or self.user_selection.upper() == "Y":
            self.is_first_roll = True
            dice = [self.die_1, self.die_2]
            print("\nWelcome!")
            self.user_selection = input("Type 'R' to roll, or any other key to quit.\nOr 'H' for help with how to play.")
            while self.user_selection is None or self.user_selection.upper() == "R" or self.user_selection.upper() == "H":
                if self.user_selection.upper() == "R"
                    for die in dice:
                        die.roll_die()

                    print("Die 1: " + str(self.die_1.current_side) + ", Die 2: " + str(self.die_2.current_side))
                    print("Your total for you roll is: " + str(self.get_die_total()))

                    self.user_selection = input("Type 'R' to roll, or any other key to quit.\n")
                else:
                    print(self.RULES)
                    self.user_selection = input("Type 'R' to roll, or any other key to quit.\nOr 'H' for help with how to play.")
            
            print("Thank you for playing!")
        else:
            print("\nOK, see you next time.")



game = Craps()