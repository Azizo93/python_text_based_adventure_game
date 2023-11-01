class Character:
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = f"{self.name} doesn't have much to say."

    def describe(self):
        print(f"{self.name} is here!")
        print(self.description)

    def talk(self):
        return (f"[{self.name} says]: {self.conversation}")

    def set_conversation(self, conversation):
        self.conversation = conversation
    
    # Fight enemy
    def fight(self, combat_item):
        print(f"{self.name} can't fight you.")
        return True
    
    def get_name(self):
        return self.name


class Enemy(Character):
    def __init__(self, char_name, char_description, defeat_message, victory_message):
        super().__init__(char_name, char_description)
        self.weakness = None
        self.stolen_items = []
        self.defeat_message = defeat_message
        self.victory_message = victory_message
        self.dropped_item = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print(self.victory_message)
            return True
        else:
            print(f"{self.name} {self.defeat_message}")
            print("GAME OVER! YOU HAVE BEEN DEFEATED")
            return False
    
    def set_dropped_item(self, item_to_drop):
        self.dropped_item = item_to_drop
    
    def get_name(self):
        return self.name
    
class FinalEnemy(Enemy):
    def __init__(self, char_name, char_description, defeat_message, victory_message):
        super().__init__(char_name, char_description, defeat_message, victory_message)
        self.weaknesses = []  # A list to store multiple weaknesses

    def set_weaknesses(self, *item_weaknesses):
        self.weaknesses.extend(item_weaknesses)

class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.hugged = False
    
    def hug(self):
        self.hugged = True
        print(f"You hugged {self.name}! They appreciate it.")
    
    def offer_gift(self, gift):
        if self.hugged:
            print(f"You offered a {gift} to {self.name}. They accept the gift with gratitude.")
        else:
            print(f"{self.name} doesn't want your gift. Hug them first!")

    def get_name(self):
        return self.name

# # To check if an object is an instance of a Friend
# if isinstance(character, Friend):
#     character.hug()  # Example usage of the hug method