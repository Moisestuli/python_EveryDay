nome = 'Moises Tulitekule'
altura = 1.80
peso = 92
imc = peso /altura**2 #IMC =  peso / (altura x altura)

# #Moises Tulitekule tem 1.80 de altura
# print(nome, 'tem' , altura , 'de altura')

# #pesa 92 quilos e seu IMC e
# print('pesa', peso, 'quilos e seu IMC e:')
# print(imc)


#formatacao
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC e:'
linha_3 = f'{imc:.2f}'


print(linha_1)
print(linha_2)
print(linha_3)



