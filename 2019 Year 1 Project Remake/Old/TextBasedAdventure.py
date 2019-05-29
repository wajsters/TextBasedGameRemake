#The random module allowing me to use the randrange function to choose random
#events and a random number to determine whether or not the player survives
import random

#Player starting coordinates
player_position = 11
#Global variable used to keep loops active, called in other functions to break the game loop
gamestate = True
#A user response function, prompts the user for a response and returns what they enter.
def user_response(question):
    """Asks the user for a response"""
    response = input(question).lower()
    return response

#Used to read a random line from the file "Events" then decides whether the user survives or dies
def event():
    """Choose a random event from file and whether the player lives or dies"""
    global gamestate
    global player_position
    
    open_event = open("Events.txt","r")
    event = open_event.readlines()
    rand_event = random.randrange(0,3)
    read_event = event[rand_event]
    print(read_event)
    open_event.close()
    fail_game = random.randrange(1,101)
    if fail_game >= 61:
        print("You failed to escape the maze")
        gamestate = False

    elif fail_game <= 60:
        print("You manage to survive!")
        rand_event = None


#This function takes the user input and decides which direction to go, also handles different symbols like
#"x" for wall or "/" for path
def go_direction(position):
    """Function used to move player around the map"""
    global player_position
    global gamestate
    # CONSTANTS
    NORTH = -10
    EAST = 1
    SOUTH = 10
    WEST = -1
    #Sets the which_direction variable to one of the variables above depending on user input
    which_direction = None
    map_file = open("Map.txt", "r")
    if position == "north":
        which_direction = NORTH
    elif position == "east":
        which_direction = EAST
    elif position == "south":
        which_direction = SOUTH
    elif position == "west":
        which_direction = WEST
    #Adds the which_direction variables value to the player_position variable to move the player around the map
    player_position += which_direction
    map_file.read(player_position)
    print_position = map_file.read(1)
    print("You move", position,"through the maze")
    #Checks to see whether they are trying to move to is a wall tile
    #If it is then it will move the player back to where they previously were and notify them
    if print_position == "x":
        player_position -= which_direction
        map_file.close()
        map_file = open("Map.txt", "r")
        map_file.read(player_position)
        print_position = map_file.read(1)
        print("There is a wall blocking your way")
        print("You head back",position)
    #If the player lands on an "E" tile it will call the event() function
    elif print_position == "E":
        event()
    #Checks to see whether the user lands on a "C" tile
    elif print_position == "C":
        print("You walk into a dimly lit room with a chest at the opposite side.")
        print("You cannot decide if you should investigate the chest further...")
        print("Will you investigate the chest?")
        #Simple loop that keeps repeating the investigate question if the user enters anything other than yes or no
        investigate = None
        while investigate not in ("yes", "no"):
            print("Please enter yes or no")
            investigate = user_response("Yes\nNo\n")
            #If the player says yes then gamestate is changed to false breaking the loop and ending the game
            if investigate == "yes":
                print("You decide to investigate the chest...")
                print("You find a key!\nAs you pick up the key the wall in front of you opens")
                print("Light floods into the room as does your memory.")
                print("Congratulations, you managed to escape the maze...")
                gamestate = False
            #If the player says no uses randrange to determine whether the play dies or survives
            if investigate == "no":
                fail_game = random.randrange(1,101)
                if fail_game >= 71:
                    print("The floor beneath you opens up, everything turns black and you keep falling...")
                    print("You failed to escape the maze")
                    gamestate = False
                elif fail_game <= 70:
                    print("You turn around and walk back",position)
                    player_position -= which_direction
                    map_file.close()
                    map_file = open("Map.txt", "r")
                    map_file.read(player_position)
                    print_position = map_file.read(1)
                    

    map_file.close()
#Main function, loops the game until gamestate is set to false
#Also handles user error by looping the user_response function incase they enter something other than a direction or exit
def Main():
    """Opens map file and allows player to move around it"""
    global gamestate
    global player_position
    while gamestate == True:
        player_move = None
        while player_move not in ("north", "east", "south", "west","exit"):
            player_move = user_response("Choose a direction to go: ").lower()
            if player_move == "exit":
                gamestate = False
            elif player_move in ("north", "east", "south", "west"):
                go_direction(player_move)
                

print("You wake up to find yourself in a small dark room.")
print("You have no recollection of how you got here or who you are.")
print("You find it difficult to see, however you spot a door in front of you.")
print("Heading south seems to be a good starting point...")
Main()
print("Thank you for playing")
input("Press enter to exit")


        
    





