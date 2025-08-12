def somar(*args): #serve para passar vários valores para uma função, sem precisar saber quantos.
    print(args)
    return sum (args)

print (somar(1,2,3,1))



def mostrar_info(**kwargs): #serve para passar vários pares chave=valor para uma função
    print(kwargs)
    

mostrar_info(nome = 'Ester', idade = 21)

print(mostrar_info)