import random
def get_dice_roll():
    return random.randint(1,6)

for i in range(1,6):
    print(get_dice_roll())