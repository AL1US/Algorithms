# Найти второе по величине число

data = [10, 5, 10, 8, 7, 8, 3]

unique = sorted(set(data), reverse=True) # set убирает дубликаты

print(unique[1])