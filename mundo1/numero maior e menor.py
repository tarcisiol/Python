x = int (input('Qual o primeiro numero?'))
y = int (input('Qual o segundo numero?'))
z = int (input('Qual o terceiro numero?'))

if x<y and x<z:
    menor = x
if y<x and y<z:
    menor = y
if z<x and z<y:
    menor = z
if x>y and x>z:
    maior = x
if y>x and y>z:
    maior = y
if z>x and z>y:
    maior = z

print (f'o menor valor digitado foi {menor}')
print (f'o maior valor digitado foi {maior}')