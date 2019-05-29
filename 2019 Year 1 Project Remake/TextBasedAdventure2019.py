import random

def get_rand(lower_val, upper_val) -> int:
    rand_val = random.randint(lower_val, upper_val)
    return rand_val

class map_obj:
    layout = ''
    map_length = 0
    
    def get_length(self):
        layout
        length = 0
        for char in self.layout:
            if char == 'x':
                length = length + 1
            else:
                break
        return length

    def display_length(self):
        return self.map_length

    def load_map(file='Map.txt') -> str:
        with open(file, 'r') as myfile:
            map_layout = myfile.read()
        return map_layout
    
    def __init__(self):
        self.layout = self.load_map()
        self.map_length = self.get_length()
   
game_map = map_obj()

length = game_map.display_length()

print(length)
