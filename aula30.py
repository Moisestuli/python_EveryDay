# lista = []
# for x in range(3):
#     for y in range(3):
#         lista.append((x,y))

# lista = [
#     (x,y)
#     for  x in range(3)
#     for y in range(3)
           
# ]

# print(lista)
# import sys

# iterable = ['eu', 'tenho','__iter__']
# iterator = iter(iterable)

# generator = (n for n in range(1000))

# print(sys.getsizeof(generator))

# for n in generator:
#     print(n)

def generator(n=0):
    yield 1 
    print('continua')
    yield 2
    return "acabou"

gen = generator()

for n in gen:
    for i in gen:
        print(n, i)


