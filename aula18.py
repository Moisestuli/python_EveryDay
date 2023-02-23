
while True:
    number1  = input('Digite um numero: ')
    number2  = input('Digite um numero: ')
    operador  = input('Digite um operador(+-/*): ')

    numross_validos = None
    num1_float = 0
    num2_float = 0

    try:
        num1_float = float(number1)
        num2_float = float(number2)
        numross_validos = True
    except :
        numross_validos = None

    if numross_validos is None:
        print('um ou ambos os numeros digitados sao invalidos.')
        continue

    operador_permitidos = '+-/*'

    if operador not in operador_permitidos:
        print('operador invalido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')

    print('Realizando sua conta, confira o valor a baixo')
    if operador == '+':
        print(num1_float + num2_float)
    elif operador == '-':
         print(num1_float - num2_float)
    elif operador == '/':
         print(num1_float / num2_float)
    elif operador == '*':
         print(num1_float * num2_float) 
    else:
        print('nunca teria chegado aqui')                  

    sair = input(' Quer sair? [s]im').lower().startswith('s')

    if sair is True:
        break      

