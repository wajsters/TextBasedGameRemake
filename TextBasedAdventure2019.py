import random

def get_rand(lower_val, upper_val) -> int:
    rand_val = random.randint(lower_val, upper_val)
    return rand_val

class map_obj:

    def __init__(self):
        self.layout = self.load_map()
        self.map_dimensions = self.load_map_config()
   
    def load_map_config(self,file='Map_Config.txt') -> list:
        map_dimensions = []
        with open(file, 'r') as myfile:
            for line in myfile:
                if 'x:' in line:
                    map_dimensions.append(line.replace('x:',''))
                elif 'y:' in line:
                    map_dimensions.append(line.replace('y:', ''))
                else:
                    map_dimensions.append(line.replace('default:', ''))
            return map_dimensions

    def display_config(self):
        for item in self.map_dimensions:
            print(item)
    
    def load_map(self,file='Map.txt') -> str:
        with open(file, 'r') as myfile:
            map_layout = myfile.read()
        return map_layout


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
            

    
# game_map = map_obj()
# 
# game_map.display_config()
