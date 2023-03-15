frase = 'tudo que eu fazer deoende de Dues'


# print(frase.count('van')) 

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes  = ''
while i < len(frase):
    letra = frase[i]

    if letra == ' ':

        continue

    qtd_apareceu_mais_vezes_actua = frase.count(letra)

    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_actua:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_actua
        letra_apareceu_mais_vezes = letra    

    i =  i + 1

    print('Aletra que apareceu mais vezes foi 'f'{letra_apareceu_mais_vezes}'' que apareceu ' f'{qtd_apareceu_mais_vezes} x')