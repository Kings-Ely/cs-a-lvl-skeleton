# Skeleton Program code for the AQA A Level Paper 1 Summer 2023 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in the Python 3.9 programming environment

from src.Dastan import Dastan


# the 'entry point' to the application, the thing that (should) get run once at the start
def main():
    # create an instance of the 'Dastan' class
    # 6 is the number of rows and columns of the board, and 4 is the number of pieces
    # as the constructor doesn't really do anything (just initialises some variables),
    # we need to call the 'PlayGame' method to actually start the game
    Dastan(6, 6, 4).PlayGame()

    # code which runs after the game has finished
    print("Goodbye!")
    input()


# this is to prevent the code from running when imported from another file,
# and prevent global variables from being created
# this is where the execution starts, everything else is a function
if __name__ == "__main__":
    main()
