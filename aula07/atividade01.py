
#meta da empresa 2000 reais

# venda = 0
# meta = 2000
# resposta = 'S'
# while resposta == 'S':
#     meta = 2000
#     venda = float(input('digite um valor: '))
#     percentual = venda / meta

#     venda += 1

#     resposta = input('quer continuar: [S/N]').upper()

meta_vendas = 2000
vendedor = 0
resposta = 'S'
while resposta == 'S':
    venda = float(input('digite um valor: '))
    nome = input('nome vendedor: ')
    atingimento = (venda / meta_vendas) * 100

    print(f'Percentual de meta {atingimento}%')
    print(f'O vendedor {nome}\nVendeu {venda}\n')

    vendedor += 1

    resposta = input('quer continuar: [S/N]').upper()