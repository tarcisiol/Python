pessoas_de_maior = 0
pessoas_de_menor = 0
ano_atual = 2026
for m in range(1,8):
    anos = int(input(f'Em que ano a {m}° pessoa nasceu? '))
    if ano_atual - anos >=18:
        pessoas_de_maior +=1
    elif ano_atual - anos <18:
        pessoas_de_menor +=1
print(f'Teremos {pessoas_de_maior} pessoas de maior e {pessoas_de_menor} pessoas de menor.')
    

