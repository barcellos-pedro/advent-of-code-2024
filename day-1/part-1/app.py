# Prototype

# arr_a = [3, 4, 2, 1, 3, 3]
# arr_b = [4, 3, 5, 3, 9, 3]

# distances = []

# arr_a.sort()
# arr_b.sort()

# ----------------------------------

import os

dir = os.path.dirname(__file__)
input_path = os.path.join(dir, 'input.txt')

list_a, list_b, distances = [], [], []

with open(input_path, 'r') as file:
    for chunk in file.read().splitlines():
        values = chunk.split(' ')

        [left_val, right_val] = list(filter(lambda it: it != '', values))

        list_a.append(int(left_val))
        list_b.append(int(right_val))

list_a.sort()
list_b.sort()

for i in range(len(list_a)):
    a, b = list_a[i], list_b[i]

    if a > b:
        distances.append(a - b)
    elif b > a:
        distances.append(b - a)
    else:
        distances.append(0)

# print(f"\nDistances: {distances}")
print(f"Total: {sum(distances)}")
