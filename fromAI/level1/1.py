# удалить все нули;
# удалить дубликаты;
# сохранить порядок первого появления чисел.

data = [4, 0, 7, 0, 2, 4, 9, 0, 2]
new_data = []

for i in data:
    if i == 0:
        continue
    if i in new_data:
        continue
    new_data.append(i)

print(new_data)



