#Inteiro para float
preco = 10
print(preco)

preco = float(preco)
print(preco)

preco = 10/2
print(preco)

#Float para inteiro
preco = 10.30
print(preco)

preco = int(preco)
print(preco)

#Conversão por divisão
preco = 10
print(preco)

print(preco / 2)

print(preco // 2)

#Numérico para sting
preco = 10.50
idade = 28

print(str(preco))

print(str(idade))

texto = f"idade {idade} preco {preco}"
print(texto)

#String para número
preco = "10.50"
idade = "28"

print(float(preco))

print(int(idade))

#Erro de conversão
preco = "python"
print(float(preco))

print(int(1.97348728))
print(int("10"))
print(float("10.10"))
print(float(100))

valor = 10
valor_str = str(valor)
print(type(valor))
print(type(valor_str))

print(type(str(10.10)))

print(100 / 2) #ponto flutuante
print(100 // 2) #parte inteira