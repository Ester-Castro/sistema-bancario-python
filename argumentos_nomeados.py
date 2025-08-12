def salvar_carro(marca,modelo,ano,placa):
    # salva carro no banco de dados ...
    print(f'Carro Inserido com sucesso! {marca}/{modelo}/{ano}/{placa}')



#salvar_carro('Fiat', 'Palio', 1999, 'ABC-1234') # não é muito vantajoso
#salvar_carro(marca='Fiat', modelo='Palio', ano=1999, placa='ABC-1234') #nomeado #tem mais vantagens que a primeira #mais ainda tem desvantagens
#salvar_carro(**{'marca': 'Fiat', 'modelo': 'Palio', 'ano': 1999, 'placa': 'ABC-1234'}) #está passando um dicionario para uma função