# for
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print() #adiciona uma quebra linha        
    print("Executa no final do laço.")

# Exemplo tabuada do 5 com a função built-in range
for numero in range(0, 51, 5)
    print(numero, end=" ")