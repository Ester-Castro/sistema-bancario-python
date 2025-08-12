nome = input('Informe o seu nome:') #entrada
idade = input('Informe a sua idade:') #entrada

print(nome, idade) #saída padrao (separada por espaço)
print(nome, idade, end='...\n') #saída com '...' no final e pula a linha
print(nome, idade, sep='a') #saída com separador '-' entre os valores