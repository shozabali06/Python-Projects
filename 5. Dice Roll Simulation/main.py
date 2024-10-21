import random
import os
import time
import sys


def getDiceRoll():
    roll = random.randrange(1, 7)
    return roll


def rollingAnimation():
    print("\nRolling ", end="")
    for i in range(3):
        time.sleep(0.8)
        sys.stdout.write("🎲")
        sys.stdout.flush()
    print()


def get_positive_integer():
    while True:
        try:
            num = int(input())
            if num > 0:
                return num
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def ask_to_roll_again():
    while True:
        opt = input("\nDo you want to roll again? (y/n): ").lower()
        if opt in ["y", "n"]:
            if opt == "y":
                return True
            else:
                return False
        else:
            print("\nInvalid input ❌. Try again.")


def getInput():
    while True:
        try:
            print("\nChoose option: ", end="")
            opt = int(input())
            if opt in [1, 2, 3, 0]:
                return opt
            else:
                print("\nInvalid integer.")
        except:
            print("\ninvalid Input. 😶")


def getMultipleRolls():
    nRolls = get_positive_integer()
    for i in range(nRolls):
        print(getDiceRoll(), end=", ")


def showMenu():
    os.system("cls" if os.name == "nt" else "clear")
    print(
        "\nWelcome to Dice Roll Simulator 🎲\n1. Roll Dice\n2. Multiple Rolls\n3. Roll until n\n0. Exit"
    )


while True:
    showMenu()
    opt = getInput()
    if opt == 1:
        rollingAnimation()
        print(f"\nYou got {getDiceRoll()}")
        while True:
            if ask_to_roll_again():
                    rollingAnimation()
                    print(f"\nYou got {getDiceRoll()}")
            else:
                break
    elif opt == 2:
        while True:
            print("Enter no of rolls: ", end="")
            nRolls = get_positive_integer()
            print("")
            rollingAnimation()
            for i in range(nRolls):
                print(getDiceRoll(), end=", ", flush=True)
            if ask_to_roll_again():
                continue
            else:
                break
    elif opt == 3:
        while True:
            while True:
                roll = 0
                print("\nChoose a target number between 1 and 6.", end=" ")
                target = get_positive_integer()
                if target <= 6:
                    rollingAnimation()
                    print("")
                    while roll != target:
                        roll = getDiceRoll()
                        print(roll, end=", ", flush=True)
                    if roll == target:
                        break
                else:
                    print("\n🛑 Choose number less than or equal to 6")
                    continue
            print("\nTarget achieved ✅")

            if ask_to_roll_again():
                continue
            else:
                break
    else:
        exit()
