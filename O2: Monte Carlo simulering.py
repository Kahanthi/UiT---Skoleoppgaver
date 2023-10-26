import random

total_points = 1000000
circle_radius = 1
square_side = 2  
number_of_hits = 0

for _ in range(total_points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 <= circle_radius**2:
        number_of_hits += 1

estimated_pi = 4 * number_of_hits / total_points

print("Estimert verdi av π er:", estimated_pi)