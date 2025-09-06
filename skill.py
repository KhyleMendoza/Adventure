import math

skills = [
    'Farming',
    'Mining',
    'Woodcutting',
    'Fishing',
    'Cooking',
    'Crafting',
    'Smithing',
    'Alchemy',
    'Archery',
    'Melee'
]

num_skills = len(skills)
varations = math.comb(num_skills, 3)

print(f"There are {varations} ways to choose 3 skills from {num_skills} skills.")
