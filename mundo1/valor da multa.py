velocidadepermitida= 80
velocidadedocarro = int (input ('Qual a velocidade do carro?'))
multa = 7
if velocidadedocarro >80: 
    print (f'voce pagara multa e o valor é: {(velocidadedocarro - velocidadepermitida) *7}')
else:
    print('nao paga multa')

