##Descobrindo quantidade de numeros impares

n = int(input(" "))
contador = 0

for i in range(1, n+1):
    total_divisores = 0
    for j in range(1, i+1):
        if i%j == 0:
            total_divisores +=1
    if total_divisores == 3:
        contador +=1
print(contador) 