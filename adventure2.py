import random

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
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def get_items(self):
        return self.items.copy()
    
    def show_description(self):
        print(f"You are in the {self.name}")
        if self.items:
            print(f"Items in this room: {self.items}")
        else:
            print("No items in this room.")

class Chest:
    def __init__(self, items, is_trap=False):
        self.items = items
        self.is_trap = is_trap
        self.trap_damage = random.randint(1, 3) if is_trap else 0
    
    def open(self, player):
        if self.is_trap:
            print(f"It was a trap chest! You lost {self.trap_damage} items!")
            removed_items = random.sample(player.inventory, self.trap_damage)
            print(f"You lost Items: {removed_items}")
        else:
            player.add_items(self.items)
        return not self.is_trap
        
class Game:
    def __init__(self):
        self.player = None
        self.rooms = {}
        self.chest = None
        self.setup_game()

    def setup_game(self):
        self.rooms = {
            "hall": Room("hall", ["key", "map"]),
            "kitchen": Room("kitchen", ["apple", "knife"]),
            "bedroom": Room("bedroom", ["potion"])
        }

        chest_items = ["iron", "copper", "silver"]
        is_trap = random.randint(1, 3)
        self.chest = Chest(chest_items, is_trap)

        player_name = input("Enter your Character name: ")
        self.player = Player(player_name)
    
    def show_room_options(self):
        print("\nWhere do you want to go?")
        room_names = list(self.rooms.keys())
        for i, room_name in enumerate(room_names, 1):
            print(f" {i}. {room_name}")

    def handle_room_movement(self):
        self.show_room_options()
        try:
            choice = int(input("Enter your choice (1-3): "))
            room_names = list(self.rooms.keys())
            if 1 <= choice <= len(room_names):
                selected_room = room_names[choice - 1]
                self.player.move_to_room(selected_room)
                self.rooms[selected_room].show_description()
            else:
                print("Invalid choice. Staying in the current room.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def open_chest(self):
        print("\nYou found a chest!")
        self.chest.open(self.player)
        self.player.show_inventory()

    def run(self):
        print("Welcome to the Adventure Game!")
        self.player.show_status()
        self.rooms[self.player.current_room].show_description()
        self.handle_room_movement()
        self.open_chest()

        print("\n=== GAME COMPLETED ===")
        self.player.show_status()
    

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()