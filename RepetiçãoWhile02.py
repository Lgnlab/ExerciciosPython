from random import randint

sorteio = randint(0, 10)
palpite = int
tentativas = 0

while palpite != sorteio:
    palpite = int(input('Seu Palpite: '))
    tentativas += 1

print(f'Você acertou com {tentativas} palpites.')