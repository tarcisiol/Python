numero = int (input ('Qual numero voce quer saber se é impar ou par?'))
resultado = numero % 2
if resultado == 0:
    print('é par')
else:
    print('é impar')