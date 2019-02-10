"""
Horse Rider Game
The player must escape the indians on their horse.
They are given various choices with various positive
and negative consequences. There are also random
chances that the player will come upon a lake to 
fill up their canteen or encounter an indian. 
"""

# imports dedent and random modules
from textwrap import dedent
import random

# game introduction
def print_intro():
    print(dedent("""
    Hey there partner!
    In attempt to escape the violent indians, you stole one
    of their horses and escaped into the prairie. 
    Gasp! You seem them chasing you in the far distance.
    Your objective: make it back to your camp 400 miles away 
    and out run the indians.
    """))


# initial assignment of variables
miles_traveled = 0
player_thirst = 0
horse_tiredness = 0
indian_distance = (-50)
drinks_in_canteen = 5


# main function
def main(miles_traveled, player_thirst,
    horse_tiredness, indian_distance, drinks_in_canteen):
    """ Main Program."""

    # calls game introduction
    print_intro()

    # main while loop
    done = False
    while not done:
        # player choices
        print(dedent("""
        What action do you choose?
        A. Take a drink
        B. Ride ahead in full speed
        C. Ride ahead in moderate speed
        D. Stop for the night.
        E. Check status
        F. Surrender to the indians
        """))

        # player choice input
        choice = input("Type in letter of your choice: ").lower().strip()

        # choice f (surrendering to the indians)
        if choice == "f":
            print(dedent("""
            The indians take back their horse and lock you up in
            their prison for the rest of your life. 
            """))
            break
        # choice e (checking status)
        elif choice == "e":
            print(dedent(f"""
            Miles Traveled: {miles_traveled}
            Miles from Camp: {400 - miles_traveled}
            Drinks in canteen: {drinks_in_canteen}
            Indians' distance in miles from you: {miles_traveled - indian_distance}
            """))
        # results from choosing choice d (stoping for night)
        elif choice == "d":
            print(dedent("""
            Both you and your horse wake up refreshed.
            But look, the indians are closer!
            """))
            horse_tiredness = 0
            indian_distance += random.randrange(5, 20)
        # results from choosing choice c (moderate speed)
        elif choice == "c":
            miles_traveled += random.randrange(5, 20)
            player_thirst += 1
            horse_tiredness += random.randrange(1, 3)
            indian_distance += random.randrange(7, 25)
        # results from choosing choice b (full speed)
        elif choice == "b":
            miles_traveled += random.randrange(10, 28)
            player_thirst += 1
            horse_tiredness += random.randrange(1, 4)
            indian_distance += random.randrange(7, 25)

        # results from choosing choice a, taking a drink
        elif choice == "a":
            if drinks_in_canteen > 0:
                player_thirst = 0
                drinks_in_canteen -= 1
                indian_distance += random.randrange(1, 3)
            elif drinks_in_canteen <= 0:
                print("You have no more drinks in your canteen")

        # checks if player at camp
        if miles_traveled > 400:
            print(dedent("""
            You made it back to camp! All the other cowboys
            shot and kill the indians that were chasing you.
            You and your new horse fall asleep with peace. 
            """))
            break

        # checks thirst of player
        # kills player if thirst above 6
        if player_thirst > 4 and player_thirst <= 6:
            print("You are getting thirsty!")
        elif player_thirst > 6:
            print("You died of thirst.")
            break

        # checks status of indians
        # ends game if indians catch up
        if (miles_traveled - indian_distance) < 15:
            print("The indians are getting close!")
        elif indian_distance > miles_traveled:
            print(dedent("""
            The Indians caught up with you.
            They take back their horse and take you to
            their prison to rot. 
            """))
            break

        # checks tiredness of horse and creates consequences
        if horse_tiredness > 6 and horse_tiredness <= 10:
            print("Your horse is getting tired, be careful.")
        elif horse_tiredness > 10:
            print(dedent("""
            Your horse died of fatigue. You see the indians
            gaining on you. You try running but you are no 
            match for their horses. They catch you and lock 
            you up in their prison to rot. 
            """))  
            break

        # random chance finding of lake and filling of canteen
        if random.randrange(20) == 0:
            print("You found an lake! You fill up your canteen.")
            drinks_in_canteen = 10

        # random chance encounter with indian
        if random.randrange(30) == 0:
            print(dedent("""
            Gasp! Another indian got ahead of the others!
            He is drawing his arrow ready to attack you.
            Do you draw your gun or run ahead?
            """))
            
            # user inputs weapon or escape
            weapon = input("Type 'gun' or 'run': ").lower().strip()
            # random response of indian
            indian_weapon = random.randrange(1, 3)

            if weapon == 'gun' and indian_weapon == 1:
                print(dedent("""
                You did not pull out your gun soon enough.
                The Indian shots you dead. 
                """))
                break
            elif weapon == 'gun' and indian_weapon == 2:
                print(dedent("""
                You shoot the indian dead. That was close!
                """))
            elif weapon == 'run' and indian_weapon == 1:
                print(dedent("""
                You were too slow for the Indian.
                The Indian shoots you down. 
                """))
                break
            elif weapon == 'run' and indian_weapon == 2:
                print(dedent("""
                You escaped the indian! That was close!
                """))
            else:
                print(dedent("""
                That wasn't a proper weapon or escape. The
                Indian shoots you dead. 
                """))
                break


# calls main function; starts game
if __name__ == '__main__':
    main(miles_traveled, player_thirst, 
    horse_tiredness, indian_distance, drinks_in_canteen)