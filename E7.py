# Crie um programa onde 4 jogadores joguem um dado e tenham resultados
# aleatórios (utilize o metodo randint do import random).
# Guarde esses resultados em um dicionário em Python. No final mostre quanto cada um dos
# jogadores tirou

from random import randint

jogadores ={'Lara': randint(1,6),'Ana Laura': randint(1,6),'Amanda': randint(1,6), 'Bianca': randint(1,6)}
print('O resultado foi: ',jogadores)