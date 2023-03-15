import os

list = []

while True:
    print('Selecione uma opção: ')
    opcao = input('[i]nserir [a]pagar [l]istar: ')


    if opcao == 'i':
        os.system('clear')
        valor = input('valor: ')
        list.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o indice para apagar: '
        )
        try:
            indece = int(indice_str)
            del list[indece]
        except:
            print('Não foi possivel apagar este indece')    
    elif opcao == 'l':
        os.system('clear')

        if len(list) == 0:
            print('Nada para listar')

        for i, valor in enumerate(list):
            print(i, valor)    

    else:
        print('Por favor, escolha i, a ou l')            