from random import randint
from time import sleep
computador = randint(0, 5)    
print('\033[1;33m-=-\033[m' * 20)
print('\033[1;34mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[1;33m-=-\033[m' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('\033[1;32mParabéns, você conseguiu me vencer!\033[m')
else:
    print(f'\033[1;31mGANHEI! Eu pensei no número {computador} e não no número {jogador}!\033[m'))
