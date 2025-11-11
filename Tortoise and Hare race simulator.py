# importing requires libraries
import random
import time

# defining starting positions of hare and tortoise as 1 to give each a fair chance
tortoise_position = 1
hare_position = 1

# tortoise movement
def tortoise_move():
    move = random.randint(1, 10)
    if 1 <= move <= 5:
        return 3  # fast plod
    elif 6 <= move <= 7:
        return -6  # slip
    else:
        return 1  # slow plod


# hare movement
def hare_move():
    move = random.randint(1, 10)
    if 1 <= move <= 2:
        return 0  # sleep
    elif 3 <= move <= 4:
        return 9  # big hop
    elif 4 < move <= 5:
        return -12  # big slip
    elif 6 <= move <= 8:
        return 1  # small hop
    else:
        return -2  # small slip


# function for race simulator
def display_race(tortoise_pos, hare_pos):
    for i in range(1, 71):
        if i == tortoise_pos and i == hare_pos:
            print("💥", end="")  # bumps into eachother
        elif i == tortoise_pos:
            print("🐢", end="")
        elif i == hare_pos:
            print("🐇", end="")
        else:
            print(" ", end="")
    print()

print("BANG !!!!!")
print("AND THEY'RE OFF !!!!!")

# determine the winner
start_time = time.time()

while True:
    hare_position += hare_move()
    tortoise_position += tortoise_move()

    if hare_position < 1:
        hare_position = 1
    if tortoise_position < 1:
        tortoise_position = 1

    display_race(tortoise_position, hare_position)

    if tortoise_position >= 70 and hare_position >= 70:
        print("It's a tie!")
        break
    elif tortoise_position >= 70:
        print("TORTOISE WINS! 🐢 SLOW AND STEADY!")
        break
    elif hare_position >= 70:
        print("HARE WINS! 🐇 QUICK BUT RECKLESS!")
        break

# calculate elapsed time
end_time = time.time()
elapsed_time = end_time - start_time
print("Time elapsed:", round(elapsed_time, 2), "seconds")