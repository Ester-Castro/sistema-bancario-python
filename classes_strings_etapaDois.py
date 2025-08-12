
nome = "Ester"
idade = 21
profissao = "Programadora"
linguagem = "Python"

saldo = 45.435

dados = {"nome": "Ester", "idade": 21} #definindo o dicionario

print("nome: %s Idade: %d" % (nome, idade)) #não utilizado com frequencia

print("nome: {} Idade: {}".format(nome, idade)) 

print("nome: {1} Idade: {0}".format(idade, nome)) 

print("nome: {1} Idade: {0} nome: {1}".format(idade, nome)) #você pode executar o nome, idade quantas vezes voce quiser, é sua vantagem

print("nome: {nome} Idade: {idade}".format(nome=nome, idade=idade)) #vantagem é passar em qualquer ordem, o que importa é o indentificador 

print("Nome: {nome} Idade: {idade}".format(**dados)) #utilizando o dicionario

print(f"Nome: {nome} Idade: {idade}") #mais utilizado

print(f"Nome: {nome} Idade: {idade} saldo: {saldo: 10.2f}") 





