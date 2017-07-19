list_items = []
class ActivitiesCrud(object):
    def __init__(self):
        self.list_items = list_items
    def create(self, item_added):
        if isinstance (item_added , str ) and item_added != "":
            for item in self.list_items:
                if item.lower() == item_added.lower():
                    raise ValueError
                else:
                    list_items.append(item_added)
    def read(self):
        return self.list_items
    def delete(self, chosen_item ):
        self.list_items.remove ( chosen_item )
        return self.list_items
    def update(self, chosen_item , new_item):
        if new_item == None or new_item == "":
            raise ValueError
        else:
            counter = 0
            while counter < len(self.list_items):
                if self.list_items[counter] == chosen_item :
                    self.list_items[counter] = new_item
                counter += 1
            return self.list_items
