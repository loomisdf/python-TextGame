from enum import Enum
import TextParser

class GameState(Enum):
    start = 0
    playing = 1
    gameOver = 2

gameState = GameState.start

while gameState == GameState.start: 
    print("Welcome to the Python Text adventure!")
    input("Press any key to continue...\n")
    gameState = GameState.playing

while gameState == GameState.playing:
    print("You are now playing the python text-based adventure game!")
    userInput = input(">") 
    TextParser.parseInput(userInput)
    
    
