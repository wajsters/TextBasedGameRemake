# Prints an ascii room from a .txt file to terminal.


def draw_room():
    with open("room_template.txt", "r") as f:
        # Create a list of rows of tiles in the room
        room = f.read().split("\n")

    # Get player position
    # ToDo: Ensure that position is positive?
    player_coordinates = Player.coordinates()
    column = player_coordinates[0]
    row = player_coordinates[1]

    # Insert player character "@" at relavent position
    player_row = "".join((room[row][:column], "@", room[row][column+1:]))
    del room[row]
    room.insert(row, player_row)

    # Create room string to print to terminal
    room_string = "\n".join(room)
    print(room_string)

