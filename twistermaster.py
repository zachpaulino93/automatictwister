#!/usr/bin/env python3

import random
import time


def gather_users():
    users = []
    loop = ""
    while len(users) <= 4:
        user = input("user name: ")
        users.append(user)
        loop = input("type yes to enter another user or no to start the game: ")
        if loop == "no":
            print("\n\n\n\n\n\n\n\ngame starting up\n\nerrrrrmmmmmm\n\n")
            time.sleep(5)
            break
    return users

def random_picks(player):
    # twister selections
    colors = random.choice(("Blue", "Green", "Yellow", "Red"))
    placment = random.choice(("Left Foot", "Right Foot", "Left Hand", "Right Hand"))
    # print selection at random
    print(f"\t{player}, place your {placment} on {colors}\n")

#def game_rounds()
# how many rounds the game will go for



def game_loop():
    users = gather_users()
    # position = random_picks(users)
    rounds_done = 1
    game_on = True
    while game_on == True:
        for player in users:
            if rounds_done <= 30:
                rounds_done += 1
                random_picks(player)
                time.sleep(5)
            else:
                contin = input("type yes to continue or no to stop: ")
                if contin == "no":
                    game_on = False
                    print("game has ended!")
                    break
                if contin == "yes":
                    rounds_done = 0
                    game_on = True
                    print("\n\n\n\n\n\nalright lets got to it! starting game!\n\n\n")
                    time.sleep(5)
                    continue




game_on = game_loop()
# print(users)
