valor = int(input('Digite o valor que sera pago: '))
print ('---MENU DE PAGAMENTO---')
print ('Digite 1 para a vista')
print ('Digite 2 para a vista no cartão')
print ('Digite 3 para 2x no cartão')
print ('Digite 4 para 3x no cartão')
opção = (int(input('De que forma voce deseja pagar? ')))
if opção == 1:
    d10 = (10 /100) * valor 
    df = valor - d10
    print(f'O valor total foi {valor} mas voce ganhou 10% de desconto e o valor sera {df}')
elif opção == 2:
    d5 = (5/100) * valor
    dd = valor - d5
    print(f'O valor total foi {valor} mas voce ganhou 5% de desconto e o valor sera {dd}')
elif opção ==3:
    print(f'O valor do produto foi: {valor}')
elif opção ==4:
    a20 = valor * (20 / 100)
    vf = a20 + valor
    print(f'Por voce escolher parcelar em mais vezes o valor saiu por {vf}')