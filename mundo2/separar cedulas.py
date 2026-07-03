valor = int(input("Digite um valor: "))
n50 = valor // 50
valor = valor % 50
n20 = valor // 20
valor = valor % 20
n10 = valor // 10
valor = valor % 10
n1 = valor
print(f"{n50} nota(s) de R$50")
print(f"{n20} nota(s) de R$20")
print(f"{n10} nota(s) de R$10")
print(f"{n1} nota(s) de R$1")