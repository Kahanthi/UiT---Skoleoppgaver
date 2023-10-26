import random

num_balls = int(input("Enter the number of balls: "))
num_slots = int(input("Enter the number of slots: "))

if num_balls <= 0 or num_slots <= 0:
    print("Please enter positive values for both balls and slots.")
else:
    slots = [0] * (num_slots + 1)

    for i in range(num_balls):
        numberOfR = 0 

        for j in range(num_slots - 1):
            direction = random.choice(["R", "L"])
            if direction == "R":
                numberOfR += 1  # Move right

        slots[numberOfR] += 1  

    
    for level in range(max(slots), 0, -1):
        for slot in slots[1:-1]:
            print('O' if slot >= level else ' ', end=' ')
        print() 

    print([1, 2, 3, 4, 5, 6, 7, 8])