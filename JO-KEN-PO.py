from random import randint
from time import sleep
jogador = 0
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
while jogador <= 2:
    jogador = int(input('Qual a sua jogada? '))
    if jogador > 2:
        print('FIM DE JOGO')
    else:
        print('JO')
        sleep(1)
        print('KEN')
        sleep(1)
        print('PÔ!!!')
        print('-=' * 12)
        print('Computador jogou {}'.format(itens[computador]))
        print('Jogador jogou {}'.format(itens[jogador]))
        print('-=' * 12)
        if computador == 0:  # COMPUTADOR JOGA PEDRA
            if jogador == 0:
                print('EMPATE!')
            elif jogador == 1:
                print('JOGADOR VENCE')
            elif jogador == 2:
                print('COMPUTADOR VENCE')
        elif computador == 1:  # COMPUTADOR JOGA PAPEL
            if jogador == 0:
                print('COMPUTADOR VENCE')
            elif jogador == 1:
                print('EMPATE!')
            elif jogador == 2:
                print('JOGADOR VENCE')      
        elif computador == 2:  # COMPUTADOR JOGA TESOURA
            if jogador == 0:
                print('JOGADOR VENCE!')
            elif jogador == 1:
                print('COMPUTADOR VENCE')
            elif jogador == 2:
                print('EMPATE')
           
