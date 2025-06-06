import random


numeros = []
for i in range(100):
    numeros.append(random.randint(1,10))


print(numeros)  
for i in range (0,len(numeros),2):
    print("indice",i,":",numeros[i])
    

numero_mayor = max(numeros)
print("el numero mayor es : ",numero_mayor)

indice_mayor = numeros.index(numero_mayor)
print("indice del numero mayor : ",indice_mayor)

numero_menor = min(numeros)
print("el numero menor es : ",numero_menor)

indice_menor = numeros.index(numero_menor)
print("indice del numero mayor : ",indice_menor)