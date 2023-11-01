class Item():
    def __init__(self, name, item_description):
        self.name = name
        self.description = item_description
        
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description

    
    def set_name(self, item_name):
        self.name = item_name

    def set_description(self, item_description):
        self.description = item_description

    def describe_item(self):
        print(self.description)

# Define the specific items within main.py
sword = Item("Sword", "An old sword, with a broken blade. It looks like it might be made of silver, perfect to use against some particularly furry creatures.")
key = Item("Key", "A small bronze key with an inscription you cannot read.")
torch = Item("Torch", "A long stick with burning material at one end, used to provide light or to set things on fire!")
orb = Item("Glowing Orb", "A mystical orb the size of an apple. It emits a bright eerie light!")
garlic = Item("Garlic", "A bulb of garlic, perfect to add some flavour to dishes or fight of vampires!")
chest = Item("Chest", "A wooden chest with a small key hole, it has the same inscription as the key.")
spell_book = Item("Spell Book", "An old leather bound book with strange ruines on the front.")
broken_mirror = Item("Broken Mirror", "A peice of a borken mirror, its sharp. It might help seeing around corners.")
# Add more items as needed


    # def get_details(self):
    #         print(self.item_name)
    #         print("-----------------------------------------")
    #         print(self.item_description)