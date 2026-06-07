salario = float (input('Qual o valor do salario?'))
desconto = float (input('Qual o valor do desconto?'))
novo_salario = salario + (salario * desconto / 100)    
print (f'o salario agora custa R${novo_salario}')
