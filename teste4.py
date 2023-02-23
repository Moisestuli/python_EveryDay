"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
"""
inicio code
numero = input('Digite um Numero inteiro: ')


if  numero.isdigit():
    int_numero = int(numero)

    par_impar = int_numero % 2 ==0
    par_impar_texto = 'impar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O numero {int_numero} e {par_impar_texto}')

else:
    print('não é um número inteiro')

    fim code
"""     
"""

Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Digite a hora : ')


try:
    int_hora = int(hora)

    if int_hora >= 0 and int_hora <= 11:
        print('Bom dia')
    elif int_hora >= 12 and int_hora <= 17:
        print('Boa tarde')     
    elif int_hora >= 18 and int_hora <= 23:
        print('Boa noite')
    else:
        print('nao conheco a hora ')
except:
    print('digita um numero inteiro') 

         
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
Nome = input('Insert you first Number: ')

qtd_letra = len(Nome)

if qtd_letra > 1:
    if qtd_letra <= 4:
        print(f'Seu nome é curto {Nome}')

    elif qtd_letra >= 5 or qtd_letra >= 6:
        print('seu nome e normal')

    else:
        print(' seu nome e londo ')    
else:
    print('digite mais de uma letra')        