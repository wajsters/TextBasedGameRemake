class Entity:
    """Entity class containing coordinates and move function."""

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def coordinates(self):
        return (self.x, self.y)

    def move(self, direction):
        if direction == "up":
            self.y += 1
        elif direction == "right":
            self.x += 1
        elif direction == "down":
            self.y -= 1
        elif direction == "left":
            self.x -= 1
