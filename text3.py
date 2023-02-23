"""
Exercicio
Peça ao usuario para digitar seu nome
Peça ao usuario para digitar sua idade

se nome e idade forem digitados:
    Exibir:
        seu nome é {nome}
        seu nome invertido é {nome invertido}
        seu nome contém (ou nao) espaço
        seu nome tem {n} letras
        A Primeira letra do seu nome é {letra}
        A ultima letra do seu nome é {letra}

se nada for digitado em nome ou idade:
    Exibir "Desculpe, voccé deixou campos vazios"               

"""
Nome = input('Digite o seu Nome: ')
Idade = input('Digite a sua idade: ')

if Nome and Idade:
    print(10 * '*--*')
    print(f'Seu nome é {Nome}')
    print(f'Seu nome invertido é {Nome[::-1]}')

    #ver espacos 
    if ' ' in Nome:
        print(f'seu nome contem espaço')
    else:
        print('seu nome nao contém espaço')
    # quantidade de letras 

    print(f'Seu Nome Tem {len(Nome)} letras')

    print(f'A primeira letra do seu nome é {Nome[0]}')
    print(f'A Ultima letra do seu nome é {Nome[-1]}')
    print(10 * '*--*')

else:
    print("Desculpe , Voçe deixou Campos vazios")

