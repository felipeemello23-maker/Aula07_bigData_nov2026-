# contador = 1
# while contador <= 10:
#     print(contador)
#     contador = contador + 1
#     #contador += 1 (também funciona faz a mesma coisa que a linha 4 )

contador = 1
soma = 0
while contador <= 5:
    n = float(input('digite um valor: '))
    soma = soma + n
    
    contador += 1

    print(f'total: {soma}')

