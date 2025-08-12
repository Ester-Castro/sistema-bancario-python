def sacar(valor): #função que tenta sacar um valor
    saldo = 500 #definimos o saldo como 500

    #bloco do if: só entra aqui se o saldo for suficiente
    # a indentação (espaço/tab) indica que esse print faz parte do if

    if saldo >= valor:
        print("valor sacado!") # este print está dentro do bloco do if

# fora da função, chamamos ela passando o valor de 500
sacar(500)