parada = cont = soma = 0

while parada != 999:
    numero = int(input('Informe um número (999 para parar): '))
    if numero == 999:
        parada = numero
    else:
        cont += 1
        soma += numero
print(f'Foram digitados {cont} números e a soma entre eles é {soma}')