# Faça um programa que o usuário vai criar um dicionário de notas.
# Ele poderá digitar a quantidade de notas que ele quiser, para parar ele deve responder
# um pergunta S/N. Ao final mostre a media das notas.

notas = {}

while True:
    a = str(input('Digite uma avaliação: '))
    notas[a] = float(input('Digite a nota: '))
    res = str(input('Deseja continuar S/N: ')).upper()
    if res == 'N':
        break
print(notas)

nota = notas.values()
nota = list(notas)

med = sum(nota)
med = med / len(nota)
print(med)