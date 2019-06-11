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
                      "cardinal directions\n(up, right, down, or left).")
        except AttributeError:
            print("Error: the move() method in Entity class requires string",
                  "input.")


# Following block is for testing Entity class
# Waj = Entity()
