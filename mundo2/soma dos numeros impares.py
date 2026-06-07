soma = 0
cont = 0
for c in range(1,501,2):
    if c %3==0:
        cont = cont + 1
        soma += c
print(f'a quantidade de valores é {cont} e a soma de todos eles é {soma}')