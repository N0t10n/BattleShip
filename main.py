from functions import BattleShip as bs
from time import sleep

# Variables
machine = bs('Machine')
user = bs(input("Write your name:"))

print(f"Hi {user.id}, let's play BattleShip!")
print("Generating boards...")
sleep(1)

# Boat length 4
user.boat_placer_loop()
print(user.board)