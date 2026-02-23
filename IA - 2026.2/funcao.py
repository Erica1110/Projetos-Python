def somar(numero_a, numero_b):
    resultado = numero_a + numero_b

    return resultado

def somar_multiplicar(numero_a, numero_b):
    resultado = (numero_a + numero_b) * 2

    soma = numero_a + numero_b
    multiplicacao = numero_a * numero_b

    return soma, multiplicacao

resultado = somar(4, 5)
print("O resultado da soma é: ", resultado)

resultado = somar("Erica ", "M.")
print("O resultado da soma é: ", resultado) 

soma, multiplicacao = somar_multiplicar(4, 6)
print("O resultado da soma é: ", soma)
print("O resultado da multiplicação é: ", multiplicacao)
