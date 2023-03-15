"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os


palavra = input('Digite a sua palavra secreta: ')
os.system('clear')
palavra_secreta = palavra
letras_acertada = ''
numero_tentativa = 0
while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativa += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra ')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertada = letras_acertada+letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'    

    print('Palavra Formada: ',palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCE GANHOU!! PARABÉNS!')
        print('A palavra era ', palavra_secreta )
        print('Numero de tentativa: ', numero_tentativa)
        # zera as variaveis 
        letras_acertada = ''
        numero_tentativa = 0

       

