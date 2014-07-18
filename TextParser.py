import sys

def parseInput(userInput):
    userInput = userInput.split()
    for x in userInput:
        if x.lower() not in commands:
            userInput.remove(x)
    if(userInput == "exit"):
        sys.exit()
    
#I'm think that this is where something is going to be printed, such as the room description
    print("")

commands = ["north","east","south","west"]
        
