"""
Repeticao

while 
executa uma accao enquanto uma condicao for verdadeiro
loop infinito -> quando um codigo nao tem fim

"""

# condicao = True

# while condicao:
#     nome = input('qual o seu nome')
#     print(f'seu nome e {nome}')

#     if nome == 'sair':
#         break
# print('Acabou')  
# contador = 0

# while contador < 20:
#     contador += 1

#     if contador == 6:
#         print('nao vou mostrar o 6')
#         continue
#     if contador % 2 == 0:
#         print('sou par')
#         continue
    

#     print(contador)

# print('acabou')   

qtd_linha = 5
qtd_Coluna = 5

linha = 1
while linha <= qtd_linha:

    coluna = 1
    while coluna <= qtd_Coluna:
        print(f'{linha=} {coluna=}')

        coluna += 1
    linha += 1
   
print('Acabou')









