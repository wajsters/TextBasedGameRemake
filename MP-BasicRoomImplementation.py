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


class Entity:
    """Entity class
    Arg1: x-coordinate of object (default = 0)
    Arg2: y-coordinate of object (default = 0)

    Methods:
    move("direction"): moves the object "up", "right", "down", or "left"
    
    """

    def __init__(self, x=1, y=1):
        self.x = x
        self.y = y
        print(f"Entity instantiated at position {self.coordinates()}")

    def coordinates(self):
        return (self.x, self.y)

    def move(self, direction):
        try:
            if direction.lower() == "up":
                self.y -= 1
            elif direction.lower() == "right":
                self.x += 1
            elif direction.lower() == "down":
                self.y += 1
            elif direction.lower() == "left":
                self.x -= 1
            else:
                print("Warning: directional input only works for the four",
                      "cardinal directions\n(up, right, down, or left).\n")

            print(f"Entity position updated to {self.coordinates()}")
        except AttributeError:
            print("Error: the move() method in Entity class requires string",
                  "input.\n")

Player = Entity()
Player.move("down")
Player.move("right")
draw_room()

