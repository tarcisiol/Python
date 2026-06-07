numero = int(input('Qual o numero? '))
unidade = numero // 1 % 10
dezena = numero //  10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print (f'O numero da unidade é: {unidade}')
print (f'O numero da dezena é: {dezena}')
print (f'O numero da centena é: {centena}')
print (f'O numero da milhar é: {milhar}')