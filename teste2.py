import random

dicionario_frutas = []


while len(dicionario_frutas) < 8:
    fruta = input('Escreva sua fruta do estoque: ')
    dicionario_frutas.append(fruta)
    break

fruta_1 = random.sample(dicionario_frutas, k=3)


print(f'1 - {fruta_1[0]} 2 - {fruta_1[1]} 3 - {fruta_1[2]}')
    