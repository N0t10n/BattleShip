from functions import BattleShip as bs
from time import sleep

# Variables
machine = bs('Machine')
user = bs(input("Write your name:"))

print(f"Hi {user.id}, let's play BattleShip!")
print("Generating boards...")
sleep(1)

# Boat length 4
# Random points
u_p = bs.rand_point(user.board, 0)
m_p = bs.rand_point(machine.board, 0)
# Random possible directions
u_d = bs.direction(user.board, u_p, user.boats[4])
m_d = bs.direction(machine.board, m_p, machine.boats[4])
# Placing it
bs.boat_placer(user.board, u_p, user.boats[4], u_d)
bs.boat_placer(machine.board, m_p, machine.boats[4], m_d)

# 2 boats length 3
u_p_3 = bs.rand_point(user.board, 0)
m_p_3 = bs.rand_point(machine.board, 0)
# Random possible directions
u_d_3 = bs.direction(user.board, u_p_3, user.boats[4])
m_d_3 = bs.direction(machine.board, m_p_3, machine.boats[4])
# Placing it
bs.boat_placer(user.board, u_p_3, user.boats[4], u_d)
bs.boat_placer(machine.board, m_p_3, machine.boats[4], m_d)

for k, v in user.boats.items():
    # Random points
    u_p = bs.rand_point(user.board, 0)
    m_p = bs.rand_point(machine.board, 0)
    # Random possible directions
    u_d = bs.direction(user.board, u_p, v)
    m_d = bs.direction(machine.board, m_p, v)
    # Placing it
    bs.boat_placer(user.board, u_p, v, u_d)
    bs.boat_placer(machine.board, m_p, machine.boats[4], m_d)