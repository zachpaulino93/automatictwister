#!/usr/bin/env python3

import random
import time


def gather_users():
    users = []
    loop = ""
    while len(users) <= 4:
        user = input("user name: ")
        users.append(user)
        loop = input("type yes to continue or no to start")
        if loop == "no":
            break
    return users

def random_picks(player):
    # twister selections 
    colors = [
    "Blue",
    "Green",
    "Yellow", 
    "Red"
      ]
    side = ["Left", "Right"]
    body = ["Hand", "Foot"]
    # print selection at random
    print(f"Alright! {player}, place {side[0]} {body[1]} on {colors[2]}\n")
    return player

#def game_rounds()
# how many rounds the game will go for



def game_loop():
    users = gather_users()
    position = random_picks(users)
    rounds_done = 0
    for rounds in range(1,100):
        if rounds_done <= 100:
            for player in users:
                rounds_done += 1
                random_picks(player)

game_on = game_loop()
# print(users)
