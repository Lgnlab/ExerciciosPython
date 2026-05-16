termos = int(input('Quantos termos você quer ver?'))
t1 , t2 = 0, 1
cont = 0

while cont < termos:
    print(t1, end=' ')
    soma = t1 + t2
    t1 = t2
    t2 = soma
    cont += 1

