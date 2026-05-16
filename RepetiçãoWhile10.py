from random import randint

cont = 0
while True:
    computador = randint(1, 10)
    pessoa = int(input('Diga um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    soma = computador + pessoa
    if soma % 2 == 0 and escolha == 'P':
        print(f'Você jogou {pessoa} e o computador {computador}. total de {soma} DEU PAR')
        cont += 1
    elif soma % 2 != 0 and escolha == 'I':
        print(f'Você jogou {pessoa} e o computador {computador}. total de {soma} DEU ÍMPAR')
        cont += 1
    else:
        if soma % 2 == 0:
            print(f'Você jogou {pessoa} e o computador {computador}. total de {soma} DEU PAR')
        else:
            print(f'Você jogou {pessoa} e o computador {computador}. total de {soma} DEU ÍMPAR')
        print(f'Você PERDEU!\nGAME OVER! Você venceu {cont} vezes.')
        break
