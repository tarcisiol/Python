palavras = ('cachorro', 'parede', 'gato', 'grama', 'chuteira', 'futebol', 'arquibancada', 'escola', 'basquete', 'celular')
for p in palavras:
    print(f'\nNa palavra {p.lower()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')