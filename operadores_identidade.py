saldo = 1000
limite = 500

print(saldo is limite) #quer saber se saldo ocupa a mesma região de memoria que limite, vai dar falso porque ambos recebem valores diferentes.

print(saldo is not limite) #quer saber se eles não ocupam a mesma região de memoria, vai dar true porque ambos recebem valores diferentes.

#mas se voce inverter os valores, e ambos serem 1000, o resultado boolean dá um resultado diferente, porque são a mesma região de memoria mas um não é complementar a outro.