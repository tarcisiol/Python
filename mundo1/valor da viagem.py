distancia = float (input ('Qual a distancia da viagem? '))
if distancia>200:
    print(f'o valor da viagem sera: {distancia * 0.45}')
else:
    print(f'o valor da viagem sera: {distancia * 0.50}')