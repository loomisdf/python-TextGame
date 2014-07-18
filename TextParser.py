import sys

def parseInput(userInput):
    userInput = userInput.split()
    print(userInput)
    for x in userInput:
        if x.lower() not in commandsList:
            userInput.remove(x)
    print("")

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
commands = ["bullshit": print("bullshit"),
            "exit": exitGame(),
            "quit": exitGame(),
            "north": north(),
            "east": east(),
            "south": south(),
            "west": west()
]
        
