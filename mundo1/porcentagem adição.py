salario = float (input('Qual o valor do salario?'))
aumento = float (input('Qual o valor do aumento?'))
novo_salario = salario + (salario * aumento / 100)    
print (f'o salario agora custa R${novo_salario}')