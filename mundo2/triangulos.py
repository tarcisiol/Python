l1 = int(input('Digite L1: '))
l2 = int(input('Digite L2: '))
l3 = int(input('Digite L3: '))
#equilatero = l1 == l2 == l3
#isosceles = l1 == l2 != l3 or l1 == l3 != l2 or l2 == l2 != l3
#escaleno = l1 != l2 != l3
if l1 == l2 == l3:
    print('é um triangulo equilatero.')
elif l1 == l2 != l3:
    print('é um triangulo isosceles.')
elif l1 == l3 != l2:
    print('é um triangulo isosceles.')
elif l2 == l3 != l1:
    print('é um triangulo isosceles.')   
elif l1 != l2 != l3:
    print('é um triangulo escaleno.')