from Classes import Item

class ItemConsumable(Item):
    def __init__(self, name, slot_size, item_type, stat_gain):
        super().__init__(name, slot_size, item_type)
        self.stat_gain = stat_gain

    def consume(self, player):
        player.stat = player.stat + self.stat_gain
