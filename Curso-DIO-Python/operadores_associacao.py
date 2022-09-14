# Objeto está presente na sequência? Maiúsculo e minúsculo faz diferença na comparação
curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

"Python" in curso
#True
print("Python" in curso)
#True

"python" in curso
#False

"maçã" not in frutas
#True
print("maçã" not in frutas)
#True

200 in saques
#False
print(200 in saques)
#False
