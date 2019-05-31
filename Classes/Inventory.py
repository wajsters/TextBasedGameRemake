class Inventory:

    def __init__(self, name='None', slot_count=0):
        self.name = name
        self.slot_count = slot_count
        self.item_collection = []
        self.slots_occupied = 0

    def inventory_status(self):
        return self.name + ':' + str(self.slot_count) + ':' + str(self.slots_occupied)

    def inventory_message(self, message):
        return self.name + ':' + message

    def pickup_item(self, item):
        new_occupied = self.slots_occupied + item.slot
        if new_occupied > self.slot_count:
            self.inventory_message(item.name + ' would exceed ' + self.name + '\'s maximum slot count')
        else:
            self.item_collection.append(item)
            self.slots_occupied = self.slots_occupied + item.slot
            self.inventory_message(item.name + ' added to inventory')

    def drop_item(self, item):
        self.slots_occupied = self.slots_occupied - item.slot
        self.inventory_status()



