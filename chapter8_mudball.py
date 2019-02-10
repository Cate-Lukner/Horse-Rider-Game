"""
This game is called "Mudball". Users take turns lobbing 
mudballs at each other until someone gets hit.
"""

import math
import random
from textwrap import dedent

def print_instructions():
    """ Prints the instructions for mudball."""

    print(dedent("""
    Howdy! Thanks for coming to play mudball! Try to hit the
    other player with a mudball. Type in the degress of your
    angle and the amount of PSI to charge your gun with.
    """))

def calculate_distance(psi, angle_degrees):
    """ Calculates the distance the mudball flies. """
    angle_radians = math.radians(angle_degrees)
    distance = (0.5 * psi ** 2 * math.sin(angle_radians) 
        * math.cos(angle_radians))
    return distance

def get_user_input(name):
    """ Get the user input for psi and angle. 
    Return as a list of two numbers."""

    try:
        psi = float(input(name + 
        ", how much psi do you want to charge your gun with? "))
        angle = float(input(name +
        ", what angle do you want to move your gun? "))
        return psi, angle
    # this doesn't work
    except:
        print("Type a number only")

def get_player_names():
    """ Get a list of names from the players. """
    print("Players! Enter your names!")
    done = False
    players = []
    while not done:
        player = input("Enter player name (hit enter to quit): ")
        if len(player) > 0:
            players.append(player)
        else:
            done = True

    return players

def process_player_turn(player_name, distance_apart):
    """ Runs the turn for each player.
    If it returns Flase, it keeps going with the game.
    If it returns True, someone has won, so it stops."""
    psi, angle = get_user_input(player_name)

    distance_mudball = calculate_distance(psi, angle)
    difference = distance_mudball - distance_apart

    if difference > 1:
        print("You went", difference, "feet too far!")
    elif difference < -1:
        print("You went", difference * -1, "feet too short!")
    else:
        print("That was a hit", player_name, "! You win!")
        return True

    return False

def main():
    """ The main program."""

    # starts the game
    print_instructions()
    player_names = get_player_names()
    distance_apart = random.randrange(50, 150)

    done = False
    while not done:
        # Loop for each player
        for player_name in player_names:
            # process each player turn
            done = process_player_turn(player_name, distance_apart)

            if done:
                break

if __name__ == "__main__":
    main()