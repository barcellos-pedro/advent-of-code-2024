import os

dir = os.path.dirname(__file__)
input_path = os.path.join(dir, 'input.txt')

list_a, list_b, occurrences = [], [], []

with open(input_path, 'r') as file:
    for chunk in file.read().splitlines():
        values = chunk.split(' ')

        [left_val, right_val] = list(filter(lambda it: it != '', values))

        list_a.append(int(left_val))
        list_b.append(int(right_val))

for value in list_a:
    appears = list_b.count(value)
    result = value * appears
    occurrences.append(result)

print(f"Total: {sum(occurrences)}")
