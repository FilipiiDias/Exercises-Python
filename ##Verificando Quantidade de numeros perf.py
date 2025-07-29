##Verificando Quantidade de numeros perfeitos

n = int(input(""))
contador = 0

for i in range (1, n+1):
    soma = 0
    for j in range(1, i):
        if i%j == 0:
            soma +=j
    if soma == i:
        contador +=1

print(contador)