import random
from item import Item, sword, key, torch, orb, garlic, chest, spell_book, broken_mirror  # Import the Item class and specific items

class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.items = []
        self.items_found = False
        self.enemy = None

    def get_description(self):
        return self.description

    def set_description(self, description):
        self.description = description

    def get_name(self):
        return self.name

    def set_name(self, room_name):
        self.name = room_name

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character
    
    def set_enemy(self, new_enemy):
        self.enemy = new_enemy

    def describe(self):
        print(self.description)

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        print(self.name)
        print("-----------------------------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.get_name()} is {direction}.")
        
        if self.enemy is not None:
            print(f"{self.enemy.get_name()} is here!")
            print(self.enemy.describe())

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way!")
            return self

    def assign_items_to_room(self, item):
        self.items.extend(item)

    def search(self):
        if self.items and not self.items_found:  # Check if there are items and they haven't been found before
            found_item = self.items.pop()  # Take the last item from the list
            self.items_found = True  # Set the items_found flag to True
            return found_item  # Return the found item
        else:
            return "Nothing to find here"  # Return this message if no item found or already found


