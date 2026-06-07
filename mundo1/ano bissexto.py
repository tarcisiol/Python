anoescolhido = int (input ('Qual o ano escolhido?'))
if anoescolhido % 4 == 0 and anoescolhido % 100 != 0 or anoescolhido % 400 ==0:
    print('é bissexto')
else:
    print('não é bissexto')