texto = input("Informe um texto: ")
VOGAIS = "AEIOU"


# Exemplo utilizando um interavel
for letra in texto: #percorre cada letra da string informada
    if letra.upper() in VOGAIS: #verifica se a letra (em maiusculo) está dentro da string de vogais
        print(letra, end="") #imprime a letra sem quebrar a linha (end="" impede a quebra de linha)

else: 
    print() #adiciona uma quebra de linha caso a letra não seja uma vogal
    print("Executa no final do laço") 



# Exemplo utilizando a função built-in range
for numero in range(0, 51, 5): #inicia do 0 até o 50(não inclui o 51 porque ele é exclusivo),pulando de 5 em 5
    print(numero, end=" ") #imprime os numeros na mesma linha, seprados por espaço