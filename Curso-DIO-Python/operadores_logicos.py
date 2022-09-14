saldo = 1000
saque = 200
limite = 100

saldo >= saque
#True

saque <= limite
#False

# Operador E
saldo >= saque and saque <= limite
#False

# Operador OU
saldo >= saque or saque <= limite
#True

# Operador de Negação
contatos_emergencia = []

not 1000 > 1500
#True

not contatos_emergencia
#True

not "saque 1500;"
#False

not ""
#True

# AND = para ser True, tudo tem que ser True
# OR = para ser True, apensa um tem que ser True

print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)

# Parênteses
saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
#True
print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
#True
print(exp_2)

conta_normal_com_saldo_suficiente = (saldo >= saque and saque <= limite)
conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saque)

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)
