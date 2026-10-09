# Раздели значения на три списка:
# отрицательные;
# равные нулю;
# положительные.


data = [-5, 12, 0, 24, -2, 18, 30, 0]
new_data = [[], [], []]

for i in data:
    if i < 0:
        new_data[0].append(i)
    elif i == 0:
        new_data[1].append(i)
    else:
        new_data[2].append(i)
    continue

print(new_data)