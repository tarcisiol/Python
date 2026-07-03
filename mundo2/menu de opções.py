escolha = 100
opção = 99
while escolha !=5:
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite o segundo numero: '))
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NUMEROS')
    print('[5] PARAR')
    escolha = int(input('Qual a sua opção: '))
    if escolha == 1:
            print(f'a soma de n1 + n2 é {n1 + n2}')
    elif escolha == 2:
            print(f'o resultado da multiplicação entre {n1} x {n2} é {n1 * n2}')
    elif escolha == 3:
            if n1 > n2:
                print(f'o maior é {n1}')
            if n1 < n2:
                print(f'o maior é {n2}')
            if n1 == n2:
                print('os numeros são iguais.')
    if escolha == 5:
            print('progama encerrado.')
        
        
