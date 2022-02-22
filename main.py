from functions import BattleShip as bs
from time import sleep

# Variables
machine = bs('Machine')
user = bs(input("Username:"))

print(f"""Hi {user.id}, let's play BattleShip!

Rules:
    -The top panel will display your boats, the bottom; your shots.
    -Wether you or the machine shoot a boat, will enjoy a second shot.
    -Win who lasts the war! Show you're smarter than a machine.

Legend:
    O: Single boat cell
    X: Boat shooted
    " ": Water
    +: Water shooted
""")
sleep(10)
print()
print("Generating boards...")
sleep(2)

# Creating boards and placing boats
machine.boat_placer_loop()
user.boat_placer_loop()
print(user.board)

m_lifes = 20
u_lifes = 20

# while m_lifes > 0 or u_lifes > 0:
#     pass
