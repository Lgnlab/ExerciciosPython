#Exercício 11
#Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mes_por_extenso de AAAA.
#Opcionalmente, valide a data e retorne None caso a data seja inválida.

def data(dia='', mes='', ano=''):
    if mes == '01':
      print(f'{dia} de Janeiro de {ano}')
    elif mes == '02':
        print(f'{dia} de Fevereiro de {ano}')
    elif mes == '03':
        print(f'{dia} de Março de {ano}')
    elif mes == '04':
        print(f'{dia} de Abril de {ano}')
    elif mes == '05':
        print(f'{dia} de Maio de {ano}')
    elif mes == '06':
        print(f'{dia} de Junho de {ano}')
    elif mes == '07':
        print(f'{dia} de Julho de {ano}')
    elif mes == '08':
        print(f'{dia} de Agosto de {ano}')
    elif mes == '09':
        print(f'{dia} de Setembro de {ano}')
    elif mes == '10':
        print(f'{dia} de Outubro de {ano}')
    elif mes == '11':
        print(f'{dia} de Novembro de {ano}')
    elif mes =='12':
        print(f'{dia} de Dezembro de {ano}')

data('23', '01', '2001')