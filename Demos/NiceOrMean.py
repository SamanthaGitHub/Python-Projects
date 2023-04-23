#
# Python:   3.8.1
#
# Author:   Samantha
#
# Purpose:  The Tech Academy - Python Course, Creating our first program.
#           Demonstrating how to pass variables from function to function.
#           while producing a functional game
#
#           Remember, function_name(variable) means we pass in the variable.
#           return variable_name means we return the value back to the function.


def start(nice=0,mean=0,name=""):
    # get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)
    

def describe_game(name):
    """
    check if this is new game or not.
    if new, gets user's name.
    if not new, thank player for playing
    and create new game
    """
    # meaning, if we do not already have this player's name,
    # they are a new player and we need to get their name.
    if name != "":
        print("\nThank you for playing again, {}".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>>").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game you will be greeted \nby several gremlins. \nYou can choose to be nice or mean to them,")
                    print("but at the end of the game your fate \nwill be sealed by the gremlins, based on your actions.")
                    stop = False
    return name


def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA gremlin approaches you for a \nsandwich. Will you be nice \nor mean? (N/M) \n>>>").lower()
        if pick == "n":
            print("/nThe gremlin walks away full and happy...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe gremlin glares at you \nmenacingly and storms off hungry...")
            mean = (mean + 1)
            stop = False
        score(nice,mean,name) # pass the three variables to the score()

def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))

def score(nice,mean,name):
    # score() is being passed the values stored in the three variables
    if nice > 2: # if the condition is valid, pass in the values to the called win()
        win(nice,mean,name)
    if mean > 2: # if condition is valid, pass in values to the called lose()
        lose(nice,mean,name)
    else: # game is still going, so call the nice_mean and pass in variables
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    print("\nNice job, {}, you win! \nThe gremlins all love you and you've \nmade lots of gremlin friends along the way!".format(name))
    # call again() and pass in variables
    again(nice,mean,name)

def lose(nice,mean,name):
    print("\nAhhh, too bad buddy, game over! \n{}, you live in a van down by the river!".format(name))
    again(nice,mean,name)

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>>".lower())
        if choice == 'y':
            stop = False
            reset(nice,mean,name)
        if choice == 'n':
            print("\nOh, so sad, sorry you have to go.")
            stop = False
            # quit() will automatically close the program
            quit()
        else:
            print("\nEnter (Y) for 'YES', (N) for 'NO':\n>>>")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    # name does not reset b/c the user decides to play again
    start(nice,mean,name)
            


            




if __name__ == '__main__':
    start()
