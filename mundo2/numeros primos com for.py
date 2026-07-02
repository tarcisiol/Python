cont = 0
np = int(input('Digite seu numero: '))
for num in range(1, np+1):
    if np%num==0:
        cont = cont +1
if cont ==2:
    print ('é primo')
else:
    print('não é primo')