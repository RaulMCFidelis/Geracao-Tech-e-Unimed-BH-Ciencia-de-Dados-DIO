# Ocupam o mesmo espaço de memória?
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso
#True

curso is not nome_curso
#False

saldo is limite
#True

saldo = 1000
limite = 500

print(saldo is limite) #Ocupam o mesmo espaço de memória?
#False

print(saldo is not limite)
#True

