#!/usr/bin/env python2.7

import random

# Rock-paper-scissors-lizard-Spock

'''
The key idea of this program is to equate the strings
"rock", "paper", "scissors", "lizard", "Spock" to numbers as follows:

0 - rock
1 - Spock
2 - paper
3 - lizard
4 - scissors
'''

# helper functions

def number_to_name(number):
    # convert number to a name
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return 'Invalid'

def name_to_number(name):
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        return 'Invalid'

def rpsls(name):
    # convert name to player_number using name_to_number()
    player_number = name_to_number(name)

    if player_number == 'Invalid':
        print "Invalid entry!!! Game exits..."
    else:
        print "Player chooses", name

        # compute random guess for comp_number using random.randrange()
        comp_number = random.randrange(0, 5)

        # convert comp_number to name using number_to_name()
        print "Computer chooses", number_to_name(comp_number)

        # compute difference of player_number and comp_number modulo five
        diff_num = (player_number - comp_number) % 5

        # determine the winner
        if diff_num == 0:
            print "Player and computer tie!"
        elif diff_num == 1 or diff_num == 2:
            print "Player wins!"
        elif diff_num == 3 or diff_num == 4:
            print "Computer wins!"
        else:
            print "Invalid result"

        print ""


# Let's play
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
