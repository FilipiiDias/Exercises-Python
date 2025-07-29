#Soma dos digitos primos de um numero

def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def soma_digitos_primos(n):
    digitos = [int(d) for d in str(n)] 
    soma = 0
    for d in digitos:
        if eh_primo(d):
            soma += d
    return soma

n = int(input(""))
resultado = soma_digitos_primos(n)
print(resultado)
