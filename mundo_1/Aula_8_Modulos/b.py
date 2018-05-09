import random
list = []
num = random.randint(1, 10)
for i in range(num):
    list.append(i)
    for j in list:
        print(list)
