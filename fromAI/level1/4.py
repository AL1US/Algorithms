# Нужно получить словарь, где ключ — название действия, значение — количество его появлений.

data = ["login", "view", "login", "purchase", "view", "logout", "purchase"]
result = {}

for i in data:
    result[i] = result.get(i, 0) + 1

print(result)

