# Prints an ascii room from a .txt file to terminal.


def create_room():
    with open("room_template.txt", "r") as f:
        # Create a list of rows of tiles in the room
        room = f.read().split("\n")

    # Insert player onto appropriate tile using their coordinates
    player_coordinates = Player.coordinates()
    if player_coordinates:
        column = player_coordinates[0]
        row = player_coordinates[1]
        room = "".join((room[row][


class Entity:
    """Entity class
    Arg1: x-coordinate of object (default = 0)
    Arg2: y-coordinate of object (default = 0)

    Methods:
    move("direction"): moves the object "up", "right", "down", or "left"
    
    """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        print(f"Entity instantiated at position {self.coordinates()}")

    def coordinates(self):
        return (self.x, self.y)

    def move(self, direction):
        try:
            if direction.lower() == "up":
                self.y += 1
            elif direction.lower() == "right":
                self.x += 1
            elif direction.lower() == "down":
                self.y -= 1
            elif direction.lower() == "left":
                self.x -= 1
            else:
                print("Warning: directional input only works for the four",
                      "cardinal directions\n(up, right, down, or left).\n")

            print(f"Entity position updated to {self.coordinates()}")
        except AttributeError:
            print("Error: the move() method in Entity class requires string",
                  "input.\n")

