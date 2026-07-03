numero = 1
while numero >=1:
    numero = int(input('Digite um numero: '))
    if numero <0:
        print('voce solicitou um valor negativo , progama encerrado.')
    elif numero ==0:
        print('voce solicitou o valor 0.')
        break
    else:
        for m in range (1,11):
            print(f'{numero} x {m} = {numero * m}')
   