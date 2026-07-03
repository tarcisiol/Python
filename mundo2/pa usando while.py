continuar = 's'
primeiro_termo = 0
razão = 1
while continuar == 's':
    primeiro_termo = int(input('Digite o primeiro termo: '))
    razão = int(input('Digite a razão da PA: '))
    for pa in range(10):
        primeiro_termo = primeiro_termo + razão
        print(primeiro_termo)
    continuar = input('Deseja calcular outra PA? (s/n): ')
print('progama encerrado.') 
    
            
    