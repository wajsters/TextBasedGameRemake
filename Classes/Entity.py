from pynput import keyboard


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

    # ToDo: Stop entities from moving beyond (1, 1) (top left corner of a room)
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



# Following line is for testing Entity class
Waj = Entity()


# ToDo: Following block of code should be called on game start, and instead
# of operating on Waj object, should operate on special player object.
def on_press(key):
    try:
        if key.char == "w":
            Waj.move("up")
        elif key.char == "d":
            Waj.move("right")
        elif key.char == "s":
            Waj.move("down")
        elif key.char == "a":
            Waj.move("left")

    except AttributeError:
        # Catches special characters, e.g. arrow keys, esc key, etc.
        #print('special key {0} pressed'.format(key))

        # Special characters currently have no function, so pass
        pass

# Collect events until released
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

