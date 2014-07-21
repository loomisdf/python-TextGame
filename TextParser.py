import sys

def parseInput(userInput):
    userInput = userInput.split()
    for x in userInput:
        if x.lower() not in commandsList:
            userInput.remove(x)

    print("")

    for x in userInput:
        c = x.lower()
        if c == "north":
            north()
        elif c == "east":
            east()
        elif c == "south":
            south()
        elif c == "west":
            west()
        elif c == "exit" or c == "quit":
            exitGame()
    

def exitGame():
    confirm = input("Are you sure? [y/n]>")
    if confirm == "y":
        sys.exit()

def north():
    print("going north")

def east():
    print("going east")

def south():
    print("going south")

def west():
    print("going west")

commandsList = ["north","east","south","west","exit"]

        
