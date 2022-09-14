from socket import NI_NUMERICHOST


while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)


# Exemplo
for numero in range(100):
    if numero == 12:
        break

    print(numero, end=" ")

# Exemplo Não exibe o 12 (...10 11 13 14...)
for numero in range(100):
    if numero == 12:
        continue

    print(numero, end=" ")

# Exemplo exibe só os números ímpares
for numero in range(100):
    if numero % 2 == 0:
        continue

    print(numero, end=" ") 

# Exemplo
while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    print(numero)       