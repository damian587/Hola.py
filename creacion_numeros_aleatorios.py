import random


numeros = []
for i in range(150):
    numeros.append(random.randint(1,100))

numeros.sort()
print(numeros)  
cont = 0
for i in range(len(numeros)):
    if numeros[i]%2==0:
        cont+=1
print(f"cantidad de numeros pares : {cont}")