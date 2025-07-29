#Contar números com soma dos divisores par


def soma_dos_divisores(num):
    soma = 0 
    for i in range (1, num+1):
        if num % i == 0:
            soma+=i
    return soma
def contar_numeros_soma_par(n):
    contador = 0
    for i in range(1, n+1):
        soma = soma_dos_divisores(i)
        if soma %2 == 0:
            contador+=1
    return contador
n = int(input(""))
resultado = contar_numeros_soma_par(n)
print(resultado)