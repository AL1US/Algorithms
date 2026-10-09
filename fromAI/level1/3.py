# сначала шли чётные числа;
# затем нечётные;
# внутри каждой группы числа шли по возрастанию.

data = [15, 2, 30, 7, 11, 4, 22, 9]
sorted_data = sorted(data)
new_data = [[], []]

for i in sorted_data:
    if i % 2 == 0:
        new_data[0].append(i)
    else:
        new_data[1].append(i)

print(new_data)