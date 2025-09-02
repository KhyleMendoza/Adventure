import random
KEY_NAME = "key"

class Player:
    def __init__(self,name):
        self.name = name
        self.inventory = ["Sword", "Gun", "Rope"]
        self.current_room = "hall"
    
    def add_items(self, items):
        if isinstance(items, list):
            self.inventory.extend(items)
        else:
            self.inventory.append(items)
        print(f"You found items: {items}")

    def remove_items(self, count):
        removed_items = []
        for _ in range(min(count, len(self.inventory))):
            if self.inventory:
                removed_items.append(self.inventory.pop(0))
        return removed_items

    def remove_random_items_excluding(self, count, exclude_items=None):
        if exclude_items is None:
            exclude_items = []
        candidates = [i for i in self.inventory if i not in exclude_items]
        if not candidates:
            return []
        take = min(count, len(candidates))
        removed = random.sample(candidates, take)
        for item in removed:
            if item in self.inventory:
                self.inventory.remove(item)
        return removed
    
    def move_to_room(self, room_name):
        self.current_room = room_name
        print(f"You are now in the {self.current_room}")

    def show_inventory(self):
        print(f"Current Inventory: {self.inventory}")

    def show_status(self):
        print(f"Player: {self.name}")
        print(f"Current Room: {self.current_room}")
        self.show_inventory()

class Room:
    def __init__(self, name, items, locked=False, required_key=None, chest=None):
        self.name = name
        self.items = items
        self.locked = locked
        self.required_key = required_key
        self.chest = chest

    def get_items(self):
        return self.items.copy()
    
    def show_description(self):
        print(f"You are in the {self.name}")
        if self.items:
            print(f"Items in this room: {self.items}")
        else:
            print("No items in this room.")

    def offer_pickup(self, player):
        if not self.items:
            return
        print("Pick up items?")
        for idx, item in enumerate(self.items, 1):
            print(f" {idx}. {item}")
        choice = input("Enter numbers separated by commas to pick up, or 0 to skip: ")
        choice = choice.strip()
        if choice == "0" or choice == "":
            return
        try:
            indices = [int(x) for x in choice.split(",")]
        except ValueError:
            print("Invalid input. Skipping pickup.")
            return
        selected = []
        for i in indices:
            if 1 <= i <= len(self.items):
                selected.append(self.items[i - 1])
        if not selected:
            print("No valid selections.")
            return
        for it in selected:
            if it in self.items:
                player.add_items(it)
                self.items.remove(it)

    def offer_open_chest(self, player):
        if not self.chest:
            return
        ans = input("There is a chest here. Open it? (y/n): ").strip().lower()
        if ans == "y":
            self.chest.open(player)
            self.chest = None

class Chest:
    def __init__(self, items, is_trap=False):
        self.items = items
        self.is_trap = is_trap
        self.trap_damage = random.randint(1, 3) if is_trap else 0
    
    def open(self, player):
        if self.is_trap:
            print(f"It was a trap chest! You lost {self.trap_damage} items!")
            removed_items = player.remove_random_items_excluding(self.trap_damage, exclude_items=[KEY_NAME])
            print(f"You lost Items: {removed_items}")
        else:
            player.add_items(self.items)
        return not self.is_trap
        
class Game:
    def __init__(self):
        self.player = None
        self.rooms = {}
        self.setup_game()

    def setup_game(self):
        chest1 = Chest(["iron", "copper"], is_trap=random.choice([True, False]))
        chest2 = Chest(["silver"], is_trap=random.choice([True, False]))
        self.rooms = {
            "hall": Room("hall", [KEY_NAME, "map"], locked=False, chest=None),
            "kitchen": Room("kitchen", ["apple", "knife"], locked=False, chest=chest1),
            "bedroom": Room("bedroom", ["potion"], locked=True, required_key=KEY_NAME, chest=chest2)
        }

        player_name = input("Enter your Character name: ")
        self.player = Player(player_name)
    
    def show_room_options(self):
        print("\nWhere do you want to go?")
        room_names = list(self.rooms.keys())
        for i, room_name in enumerate(room_names, 1):
            room = self.rooms[room_name]
            if room.locked and room.required_key and room.required_key not in self.player.inventory:
                print(f" {i}. {room_name} (locked)")
            else:
                print(f" {i}. {room_name}")

    def handle_room_movement(self):
        self.show_room_options()
        try:
            choice = int(input("Enter your choice (1-3): "))
            room_names = list(self.rooms.keys())
            if 1 <= choice <= len(room_names):
                selected_room = room_names[choice - 1]
                room = self.rooms[selected_room]
                if room.locked and room.required_key and room.required_key not in self.player.inventory:
                    print(f"The {selected_room} is locked. You need a {room.required_key}.")
                else:
                    if room.locked and room.required_key in self.player.inventory:
                        print(f"You use the {room.required_key} to unlock the {selected_room}.")
                        room.locked = False
                    self.player.move_to_room(selected_room)
                    room.show_description()
                    room.offer_pickup(self.player)
                    room.offer_open_chest(self.player)
            else:
                print("Invalid choice. Staying in the current room.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def run(self):
        print("Welcome to the Adventure Game!")
        self.player.show_status()
        self.rooms[self.player.current_room].show_description()
        self.handle_room_movement()

        print("\n=== GAME COMPLETED ===")
        self.player.show_status()
    

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()