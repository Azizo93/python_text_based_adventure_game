from room import Room
from character import Character, Enemy, Friend, FinalEnemy
from item import Item, sword, key, torch, orb, garlic, chest, spell_book, broken_mirror # Import the Item class and specific items
from game_variables import Inventory

game_name = "The Castle of 'DARKNESS'"

player_inventory = Inventory()
player_defeated = False
first_item_found = False
defeated_enemies = []
undercroft_revealed = False
found_chest = False
found_key = False
has_spell_book = False

# Define the reset_game function
# def reset_game():
#     player_inventory.items = [] # Reset the player's inventory to an empty list

grand_entrance = Room("Grand Entrance")
grand_entrance.set_description("The entrance to an old castle. It is damp and cold. The large staircase is blocked by the collaped roof but the light of the moon reveals two old wooden doors, tread wisely.")

kitchen = Room("kitchen")
kitchen.set_description("A dank and dirty room covered in mould & buzzing with flies.")

ball_room = Room("Ball Room")
ball_room.set_description("A once grand Ball Room, now with dusty chandeliers. A large tapestry hangs along the southern wall.")

dining_hall = Room("Dining Hall") 
dining_hall.set_description("A dining hall with a long table pushed against the remains of wooden door. Golden plates of rotting food are everywhere! A flickering torch reveals damaged portraits barely hanging on the walls.")

undercroft = Room("Undercroft")
undercroft.set_description("A secret room hidden behind the Ball Room tapestry. There must be something of value here!")

grand_entrance.link_room(kitchen, "east")
kitchen.link_room(dining_hall, "south")
kitchen.link_room(grand_entrance, "west")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ball_room, "west")
ball_room.link_room(dining_hall, "east")
ball_room.link_room(grand_entrance, "north")
undercroft.link_room(ball_room, "north")
grand_entrance.link_room(ball_room, "south")

wizard = Friend("The Old Wizard", "A frail old wizard here to guide you on your journey.")
grand_entrance.set_character(wizard)
wizard.set_conversation("Welcome traveller, I foresaw your arrival and require your help.\n This once great castle has been taken over by evil entities.\n I seek your help in defeating these creatures and obtaining my spell book. It has been stolen from me and is locked in a chest guarded by one of these foul creatures.\n Venture though this old castle and locate the key to the chest.\n Once you have the key you must find the chest and defeat its protector.\n Return with my spell book and together we can save this castles inhabitants.\n Only YOU can save this castle from THE DARKNESS!")

the_cook = Character("The Cook", "His body looks like it has been drained of blood.")
the_cook.set_conversation("The Cook doesn't appear to be in a very talkative mood.")
kitchen.set_character(the_cook)


nibbler = Enemy("Nibbler", "A smelly zombie, hungry for BRAINS!", "is unaffected he takes his chance and attacks! You have tasty brains!", "You swing your torch at Nibbler and he erupts into a ball of flames! Only a pile of ash remains.")
nibbler.set_dropped_item(key)
dining_hall.set_character(nibbler)
nibbler.set_conversation("ARGHGHHGGH... BRAINS! BRAINS! NIBBLER WANTS BRAINS!")
nibbler.set_weakness(torch)

mooney = Enemy("Mooney", "A vicious Werewolf, with blood soaked fur.", "looks amused as he lunges for you! It looks like you will be busy when the full moon come out in future!", "You swing your silver sword at Mooney and he howls as he sheds his fur and before you lies the lifeless body of the man he once was!\nAs you defeat Mooney, you notice a glowing orb dropped by him. \nThis might be useful; maybe you should take it.")
mooney.set_dropped_item(orb)
ball_room.set_character(mooney)
mooney.set_conversation("GRRRRRRRRR HAWOOOOOOO, I will rip the flesh from your bones!")
mooney.set_weakness(sword)

vlad = FinalEnemy("Vlad", "An ancient vampire. He looks strong!", "is unfazed by your attach. He laughs and lunges for your thoat!", "You raise the orb as it pulsates brighter and brighter, Vlad is weakening!\nYou charge with garlic in hand and shove it into the vampires mouth! Vlad shreeks as his skin turns translucent and then to dust!")
vlad.set_dropped_item(chest)
undercroft.set_character(vlad)
vlad.set_conversation("Ahhhh, Welcome traveller, it appers you have defeated my minions. I on the otherhand will not be so easily vanquished. You will not have what you seek!")
vlad.set_weaknesses(orb, garlic)

# Assign items to specific rooms
grand_entrance.items.append(sword)
kitchen.items.append(garlic)
dining_hall.items.append(torch)
ball_room.items.append(broken_mirror)

# Define the select_item_from_inventory function
def select_item_from_inventory(inventory):
    if not inventory.get_items():
        print("Your inventory is empty. You have no items to use.")
        return None

    print("Your Inventory:")
    item_names = [item.get_name().lower() for item in inventory.get_items()]
    for index, item in enumerate(inventory.get_items(), start=1):
        print(f"{index}. {item.get_name()} - {item.get_description()}")

    while True:
        choice = input("Select an item by typing its name (or 'cancel' to cancel): ").strip().lower()
        if choice == 'cancel':
            return None  # Player canceled
        for index, item_name in enumerate(item_names, start=1):
            if item_name == choice:
                return inventory.get_items()[index - 1]  # Return the selected item
        print("Item not found in your inventory. Please type the item name or 'cancel'.")



# Welcome Notes and Player Name Input
print("Welcome to 'The Castle of 'DARKNESS' - A Text-Based Adventure Game!")
player_name = input("Before we begin, what's your name? ")

player_age = int(input(f"It is nice to meet you {player_name}. Please can you confirm your age?: "))
# Check the player's age
if player_age < 18:
    print(f"Sorry {player_name}, you are currently {player_age}. You must be at least 18 years old to play {game_name}.")
    exit()  # Exit the game if the player is too young
print("\n")
print(f"Greetings {player_name}! \nYou find yourself at the grand entrance of an old castle.")
print("The castle is filled with mysteries, challenges, and a great quest.")
print("Your goal is to explore, interact with characters & solve the mysteries of the castle.\n")
print(f"The fate of the castle rests in your hands. So {player_name}, let's embark on this adventure!")


current_room = grand_entrance

# Define the game loop
while True:
    while not player_defeated:
        print("\n")
        current_room.get_details()
        inhabitant = current_room.get_character()

        # Check if the inhabitant is an enemy and not already defeated
        if isinstance(inhabitant, Enemy) and inhabitant not in defeated_enemies:
            inhabitant.describe()
        elif inhabitant is not None and inhabitant != mooney:  # Check if it's not an enemy or not Mooney
            inhabitant.describe()

        # Check if the "Undercroft" should be revealed
        if inhabitant is not None and inhabitant == mooney and not undercroft_revealed:
            undercroft_revealed = True  # Set the flag to reveal the "Undercroft"

        print("What would you like to do? Go - North, East, South, West? 'talk', 'fight', 'search' 'back' or 'interact'?")
        command = input("\n> ").lower()
        
        if command == "interact" and current_room != undercroft and chest not in player_inventory.get_items():
            print("There is nothing to interact with here, please use a different command.")
        elif command == "interact" and current_room == undercroft and chest not in player_inventory.get_items():
            print("There is nothing to interact with right now. You could always try again later if needed.")
        if command == "back" and current_room == ball_room and chest in player_inventory.get_items():
            print("You decide to go back to the Undercroft.")
            current_room = undercroft
        elif command == "back" and current_room == ball_room and orb and garlic in player_inventory.get_items():
            current_room = undercroft 
        elif command == "back" and current_room == ball_room and chest not in player_inventory.get_items():
            print("It doesn't look like there is any where to go back to right now. Maybe try again later.")
            current_room = ball_room
        elif command == "back":
            print("You can't go back from this room, please use a different command.")
        # elif command == "search":
        #     current_room.search()

            

        # Check the player's input
        if command in ["north", "south", "east", "west"]:
            current_room = current_room.move(command)
        
        elif command == "fight":
            if current_room.get_character() is not None:
                character_in_room = current_room.get_character()
                if isinstance(character_in_room, Enemy) and character_in_room not in defeated_enemies:
                    if character_in_room == vlad:  # Check if the enemy is Vlad
                        has_orb = any(item.get_name() == "Glowing Orb" for item in player_inventory.get_items())
                        has_garlic = any(item.get_name() == "Garlic" for item in player_inventory.get_items())

                        if has_orb and has_garlic:
                            # Player has both the orb and garlic, they can defeat Vlad
                            print(f"You use the Orb and Garlic from your inventory to defeat {character_in_room.get_name()}!")
                            character_in_room.fight(None)  
                            defeated_enemies.append(character_in_room)
                            dropped_item = character_in_room.dropped_item
                            if dropped_item:
                                player_inventory.add_item(dropped_item)
                                print(f"You make your way past the vampires remains. AT LAST! There is the {dropped_item.get_name()} that {character_in_room.get_name()} was guarding. It must contain the Spell Book.")
                                found_key = True
                            current_room.set_character(None)
                            found_chest = True
                            if found_chest and found_key:
                                print("You approach the chest and see that it has strange markings simmilar to those on the key you found earlier.")

                                if key in player_inventory.get_items():
                                    print("You have the key in your inventory. Would you like to use the key to open the chest? (yes/no)")
                                    use_key = input("Type 'yes' or 'no': ").lower()

                                    if use_key == "yes":
                                        has_spell_book = True
                                        def open_chest():
                                            if key in player_inventory.get_items():
                                                print("You use the key to open the chest.")
                                                # Add logic to handle what's inside the chest
                                                print("Inside the chest, you find the wizard's spell book.\nIt has been added to your inventory.")
                                                print(f"{player_name} you should head back to the Old Wizard and return his Spell Book.")
                                                player_inventory.add_item(spell_book)
                                                
                                            else:
                                                print("You don't have the key to open the chest.")

                                        open_chest()
                                    else:
                                        print("You decide not to open the chest for now.")

                            if character_in_room == mooney:
                                if undercroft_revealed:
                                    print("The fight with Mooney was tough. You look around and have nowhere to go.")
                                    print("All of a sudden the room begins to shake.")
                                    print("The strange tapestry on the wall falls to the ground to reveal a hidden room.")
                                    print("Maybe it's worth investigating...")
                                    current_room.set_character(None)  # Remove Mooney from the room
                                    current_room = undercroft
                            

                        else:
                            print("You will need to be better equipped to defeat Vlad. Keep exploring the castle to find the items you need. You can always come 'back' to the undecroft from the Ball Room.")
                    else:
                        # Normal enemy fight logic
                        combat_item = select_item_from_inventory(player_inventory)
                        if combat_item is not None:
                            if combat_item == character_in_room.weakness:
                                print(f"You use the {combat_item.get_name()} to defeat {character_in_room.get_name()}!")
                                character_in_room.fight(combat_item)
                                defeated_enemies.append(character_in_room)
                                dropped_item = character_in_room.dropped_item
                                if dropped_item:
                                    player_inventory.add_item(dropped_item)
                                    print(f"You found a {dropped_item.get_name()} after defeating {character_in_room.get_name()}, it has been added to your inventory!")
                                current_room.set_character(None)
                                if character_in_room == mooney and undercroft_revealed:
                                    print("The fight with Mooney was tough. You look around and have no where to go.")
                                    print("All of a sudden the room begins to shake.")
                                    print("The strange tapestry on the wall falls to the ground to reveal a hidden room.")
                                    print("Maybe it's worth investigating...")
                                    current_room = undercroft
                            else:
                                print(f"The {combat_item.get_name()} is not effective against {character_in_room.get_name()}.")
                                print(f"{character_in_room.get_name()} {character_in_room.defeat_message}")
                                player_defeated = True
                                print("GAME OVER. You have been defeated.")
                        else:
                            print("You chose to cancel the fight.")
                else:
                    print(f"{character_in_room.get_name()} does not want to fight you.")
            else:
                print("There's no one to fight here.")


        elif command == "search":
            search_result = current_room.search()
            if isinstance(search_result, str):
                print(search_result)
            else:
                if not first_item_found:
                    print("Congratulations, you have found your first item. Items can be used to help defeat enemies.")
                    print("Choose your item wisely to ensure you are not defeated.")
                    first_item_found = True
                player_inventory.add_item(search_result)
                print(f"You found a {search_result.get_name()}. {search_result.get_description()}. The item has been added to your inventory.")

        elif command == "talk":
            if current_room.get_character() is not None:
                character_in_room = current_room.get_character()
                if character_in_room == wizard:
                    if has_spell_book:
                        print("You approach the wizard with the spell book.")
                        print(f"You have found your way through the castle and defeated the evil creatures. You now deliver the spell book to the wizard.")
                        print("The wizard is delighted and grateful.")
                        print("\n")
                        print("Wizard: Thank you brave adventurer. You have successfully completed this quest!")
                        print("The wizard opens the spell book and begins casting his magical spells.\nAll of a sudden there is a bright light and the castle changes before your eyes as it is restored to its former glory.")
                        print("\n")
                        print(f"Wizard: Congratulations {player_name}! You have saved the castle and its many residents from this terrible evil.\n")
                        print("You may have defeated 'THE DARKNESS' But your journey has just begun.\n")
                        print(f"Thank you for playing 'The Castle of 'DARKNESS'. farewell {player_name}!")
                        exit()  # Exit the game, as the player has won
                    else:
                        print(character_in_room.talk())
                else:
                    print(character_in_room.talk())
            else:
                print("There's no one to talk to here.")
                
        # Check for interacting with the chest
        elif command == "interact" and current_room == undercroft:
            if key in player_inventory.get_items():
                # Add logic to handle what's inside the chest
                if found_chest and found_key:
                                print("You approach the chest and see that it has strange markings simmilar to those on the key you found earlier.")

                                if key in player_inventory.get_items():
                                    print("You have the key in your inventory. Would you like to use the key to open the chest? (yes/no)")
                                    use_key = input("Type 'yes' or 'no': ").lower()

                                    if use_key == "yes":
                                        has_spell_book = True
                                        def open_chest():
                                            if key in player_inventory.get_items():
                                                print("You use the key to open the chest.")
                                                # Add logic to handle what's inside the chest
                                                print("Inside the chest, you find the wizard's spell book.\nIt has been added to your inventory.")
                                                print(f"{player_name} you should head back to the Old Wizard and return his Spell Book.")
                                                player_inventory.add_item(spell_book)
                                                
                                            else:
                                                print("You will need to keep searching.")

                                        open_chest()
                                    else:
                                        print("You decide not to open the chest for now.")
                                else:
                                    print("You will need to find the key if you wish to open the chest.")        
            else:
                print("You should keep searching the castle.")

        # Player is defeated, update the game state accordingly
        if player_defeated:
            while True:
                play_again = input("Do you want to play again? (yes/no): ").lower()
                if play_again == "yes":
                    player_defeated = False  # Reset the player's defeated status
                    current_room = grand_entrance  # Reset to the starting room
                    break
                elif play_again == "no":
                    print("Thank you for playing 'The Castle of 'DARKNESS'. Goodbye!")
                    exit()  # Exit the game
                else:
                    print("Please enter 'yes' or 'no.")


    # End of the main game loop
