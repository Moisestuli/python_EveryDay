nome = 'Moises tulitekule'

indece = 0
novo_nome  = ''

while indece < len(nome):
    letra = nome[indece]
    novo_nome += f'*{letra}'

    indece += 1

novo_nome += '*'
print(novo_nome)    