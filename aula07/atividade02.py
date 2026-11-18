contador = 0
gasto = 0
soma = 0

while True:
    numero = int(input('informe a despesa '))
    contador += 1
    soma = numero + soma

    resposta = input('\nQuer continuar: [S/N]').upper()
   

    if resposta  == 'N':
        break

print(f'Quantidade de despesas registradas {contador}\n Valor total {soma}')


 