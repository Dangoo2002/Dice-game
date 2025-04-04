import random

rolls = 1000

dice_gen = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}


for _ in range(rolls):
    roll = random.random() * 6  

    if 0 <= roll < 1:
        dice_gen[1] += 1
    elif 1 <= roll < 2:
        dice_gen[2] += 1
    elif 2 <= roll < 3:
        dice_gen[3] += 1
    elif 3 <= roll < 4:
        dice_gen[4] += 1
    elif 4 <= roll < 5:
        dice_gen[5] += 1
    else:  
        dice_gen[6] += 1  

# Calculate percentages 
percentages = {}
for face in dice_gen:
    percent = (dice_gen[face] / rolls) * 100
    percentages[face] = round(percent, 2)


print("| {:<8} | {:<10} | {:<10} |".format("Face", "Frequency", "Percent"))
print("-" * 32)
for face in dice_gen:
    print("| {:<8} | {:<10} | {:<10.2f}% |".format(face, dice_gen[face], percentages[face]))

print("-" * 32)
print("| {:<8} | {:<10} | {:<10.2f}% |".format("Total", rolls, 100.0))
