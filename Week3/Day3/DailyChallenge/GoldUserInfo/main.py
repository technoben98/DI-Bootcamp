user_data = []
for _ in range(5):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    score = int(input("Enter score: "))
    user_data.append((name, age, score))

user_data.sort(key=lambda x: (x[0], x[1], x[2]))
print(user_data)