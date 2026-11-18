
while True:
    numero = int(input('informe um numero '))
    
    dobro = numero * 2
    triplo = numero * 3
    quadrado = numero ** 2
    
    print(f'Dobro: {dobro}\nTriplo: {triplo}\nQuafrado: {quadrado}')
    
    resposta = input('\nQuer continuar: [S/N]').upper()

    if resposta == 'N':
        break
    