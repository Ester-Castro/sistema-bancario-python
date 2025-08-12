opcao = 1 #valor inicial diferente de 0 para entrar no loop

while opcao != 0: # o loop continua enquanto a opcao for diferente de 0
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: ")) # solicita uma opção do usuário e converte para inteiro

    if opcao == 1: # se a opção for 1,executa a ação sacar.
        print("Sacando ...")

    elif opcao == 2: #se a opcão for 2,exibe o extrato
        print("Exibindo o extrato ...")

else: #exibe a mensagem ao apertar 0 quando sair, sempre no final do laço
    print("Obrigado por usar nosso sistema bancário, até breve!")