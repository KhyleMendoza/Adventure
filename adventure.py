inventory = ["Sword", "Gun", "Rope"]

chest = ["iron", "copper", "silver"]
trap_chest = 3
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

print("Inventory: ", inventory)

for _ in range(trap_chest):
    if inventory:
        inventory.pop()
print("It was a trap chest you lost 3 items!")

print("Inventory:", inventory)
