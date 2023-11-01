class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if item not in self.items:  # Check if the item is not already in the inventory
            self.items.append(item)

    def get_items(self):
        return self.items

    def remove_item(self, item):
        self.items.remove(item)

    def show_inventory(self):
        if not self.items:
            print("Your inventory is empty. You have no items.")
        else:
            print("Your Inventory:")
            for item in self.items:
                print(f"- {item.get_name()} - {item.get_description()}")

    def get_item_names(self):
        return [item.get_name().lower() for item in self.items]
