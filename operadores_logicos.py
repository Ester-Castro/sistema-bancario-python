 #AND nessa condição pra ser true, tudo tem que ser true
 #OR nessa condição pra ser true, pelo menos um precisa ser true



print(True and True) #verdadeiro
print(True and False) #Falso
print(False and False) #Falso
print(True or True) #verdadeiro
print(True or False) #verdadeiro
print(False or False) #Falso


saldo = 1000
saque = 250
limite = 200
conta_especial = True

esp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque

print(esp)

esp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

print(esp_2)


#essa ultima expressao torna o codigo mais legivel!!!

conta_normal_com_saldo_suficiente = (saldo >= saque and saque <= limite) 
conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saque)

esp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente

print(esp_3)


