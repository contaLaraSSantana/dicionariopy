#coleção não ordenada de elementos onde é acessado por uma {} unica

#biblioteca consegue nomear as chaves

#pessoa = {'Nome':'Duda', 'Idade':16,'Altura':1.50}
#print(pessoa['Nome'])

#pessoa = {}
#pessoa = dict()- vazio
#Nem todas as funções de lista funcionam

#pessoa['Peso'] = 60.5 #add item
#del pessoa['Peso']

#fatiamento
pessoa = {'Nome':'Duda', 'Idade':16,'Altura':1.50}
pessoa2 ={'Nome':'Brenda','Peso':60,'Sexo':'F'}
pessoa.update(pessoa2)
print(pessoa2)
pessoa2['Peso'] = 52
print(pessoa2)

print(pessoa.values()) #Brenda
print(pessoa.keys()) #Nome
print(pessoa.items())

#imprime um embaixo do outro

for K in pessoa.keys():
    print(K)

for V in pessoa.values():
    print(V)

for K,V in pessoa.items():
    print(f'O item{K} é {V}')

idaded= int(input('Digite sua idade:' ))
if idaded in pessoa.values():
    print('Idade igual a da Duda')


