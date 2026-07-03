totalgasto = 0
mais_de_mil = 0
mais_barato = ''
valor = 0
produto_ = 0
continuar = 's'
while True:
    produto = input('Qual o nome do produto? ').upper()
    valor = int(input('Valor R$:'))
    totalgasto = totalgasto + valor
    if valor > 1000:
        mais_de_mil += 1
    if totalgasto == valor:
        produto_ = valor
        mais_barato = produto
    else:
        if valor < produto_:
            produto_ = valor
            mais_barato = produto
    continuar = input('Deseja cadastrar mais produtos? (S/N): ').lower()
    if continuar != 's':
        break
print(f'O TOTAL GASTO FOI {totalgasto}')
print(f'{mais_de_mil} PASSARAM DE MIL REAIS')
print(f'O PRODUTO MAIS BARATO FOI {mais_barato}')