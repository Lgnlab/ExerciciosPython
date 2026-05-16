parada = 'S'
maior = menor = soma = cont = 0
while parada == 'S':
    numero = int(input('Informe um número: '))
    soma += numero
    cont += 1
    if cont == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    parada = str(input('Quer continuar(S/N)? ')).upper().strip()[0]

print(f'Média: {soma / cont:.1f}')
print(f'Maior: {maior}\nMenor: {menor}')