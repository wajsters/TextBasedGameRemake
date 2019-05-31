from Classes import Item


class Apple(Item):
    def __init__(self, name, slot_size, item_type):
        super().__init__(name, slot_size, item_type)
