import time
import pyautogui as auto
from time import sleep
import colorama
from colorama import Fore, Style
colorama.init()

def spammer():
    clear = lambda: os.system('cls')
    clear()

print('\033[031m')
us = input("username: ")
print()
print('\033[031m' + 'Made By')
print("""ooooooo  ooooo #oooooo   oooo #  .oooooo.   # oooooooooooo #
 `8888    d8'  # `888.   .8'  # d8P'  `Y8b  #d'""""""d888' #
   Y888..8P    #  `888. .8'   #888          #      .888P   #
    `8888'     #   `888.8'    #888          #     d888'    #
   .8PY888.    #    `888'     #888          #   .888P      #
  d8'  `888b   #     888      #`88b    ooo  #  d888'    .P #
o888o  o88888o #    o888o     # `Y8bood8P'  #.8888888888P  #
               #              #             #              #
               #              #             #              #
               ##              ##             ##              ##""")
choice = input("""
{1} Run Spammer

: """)

def c():

  if choice == "1":
    print()
print("Press {Enter} to wr!te the mess@ge you wanna $pam to that k1d!")
input()
Sp = input("What you wann $pam?: ")
print()
print("Loading...")
sleep(5.0)
print()
Ac = input("---PRESS {EMTER} TO $PAM THAT S0N OF A B!TCH---")
print()
print('\033[32m' + 'Loading...')
sleep(3.0)
print('\033[31m')
while True:
        auto.write(Sp)
        auto.press('enter')
        sleep(0.001)
        print("GET SPAMMED BY",us)
