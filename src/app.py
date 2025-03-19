import random
a = []
for x in range(1, 1000000):
        random_number = random.randint(0,255)
        a.insert(x, random_number)


b = []
for x in range(1, 1000000):
        random_number = random.randint(0,255)
        a.append(x, random_number)

def hello():
        print("hello")