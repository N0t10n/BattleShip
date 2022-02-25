from functions import BattleShip as bs
from time import sleep

# Variables
machine = bs('Machine', 'easy')
user = bs(input("Username: "))

print(f"""Hi {user.id}, let's play BattleShip!

Rules:
    -The top panel will display your boats, the bottom; your shots.
    -Wether you or the machine shoot a boat, will enjoy a second shot.
    -Win who lasts the war! Show you're smarter than a machine.

Legend:
    O: Single boat cell
    \033[91m'X'\033[0m: Boat shooted
    ' ': Water
    \033[94m+\033[0m: Water shooted
""")
sleep(1)
print("Generating boards...")
sleep(5)
print()

# Creating boards and placing boats
machine.boat_placer_loop()
user.boat_placer_loop()
user.board_printer()

while machine.life > 0 and user.life > 0:

    try:
        print('Your turn:')
        user.shooting(machine)
        user.board_printer()

        print()
        sleep(2)

        print('Machine turn:')
        print(f'\tRemaining {machine.id} lifes: {machine.life}')
        machine.shooting(user, 'easy')
        user.board_printer()

    except:
        break

if machine.life == 0:
    print('\nAwesome! You showed that bastard humans still are in the top chain.')

else:
    print('\nYou lose.\nEnjoy your last days... This is the beginning of a machine revolution.')