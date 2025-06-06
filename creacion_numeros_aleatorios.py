import random


numeros = []
for i in range(100):
    numeros.append(random.randint(1,100))

numeros.sort()
print(numeros)  