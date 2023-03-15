
# for letra in texto
# texto  = 'Moises' # iteravel
# iterador = iter(texto) #iterator

# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#         break    

#for letra in texto:
 #   print(letra)

for i in range(10):
    if i ==2:
        print('i e 2, pulando....')
        continue

    if i == 8:
        print('i e 8, seu else nao executara')
        #break

    for j in range(1, 3):
        print(i, j)

else:
    print('for completo com sucesso ')