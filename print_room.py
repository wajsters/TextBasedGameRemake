# Prints an ascii room from a .txt file to terminal.


def print_room():
    with open("room.txt", "r") as f:
        room = f.read()

