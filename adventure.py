import random

inventory = ["Sword", "Gun", "Rope"]

chest = ["iron", "copper", "silver"]
trap_chest = random.randint(1, 3)
room = {
    "hall": ["key", "map"],
    "kitchen": ["apple", "knife"],
    "bedroom": ["potion"]
}
current_room = "hall"
print(f"You are in the {current_room}")
print("Current Inventory: ", inventory)
print("Where do you want to go? \n 1.Hall \n 2.Kitchen \n 3.Bedroom")


for item in chest:
    inventory.append(item)

print("You found items:", chest)
print("Inventory: ", inventory)

for _ in range(trap_chest):
    if inventory:
        inventory.pop()
print(f"It was a trap chest you lost {trap_chest} items!")
print("Inventory:", inventory)
