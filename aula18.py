
while True:
    number1  = input('Digite um numero: ')
    number2  = input('Digite um numero: ')
    operador  = input('Digite um operador(+-/*): ')

    numross_validos = None

    try:
        num1_float = float(number1)
        num2_float = float(number2)
        numross_validos = True
    except :
        numross_validos = None

    sair = input(' Quer sair? [s]im').lower().startswith('s')

    if sair is True:
        break      

