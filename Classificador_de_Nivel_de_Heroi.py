heroi = input('Digite o nome do heroi: ')
print('Olá, ' + heroi)
exp = int(input('Digite o exp acumulado: '))
if exp <= 1000:
    print('Sua classificação é Ferro')
if ((exp >= 1001) and (exp <= 2000)):
    print('Sua classificação é Bronze')
if ((exp >= 2001) and (exp<= 5000)):
    print('Sua classificação é Prata')
if ((exp >= 5001) and (exp <= 7000)):
    print('Sua classificação é Ouro')
if ((exp >= 7001) and (exp <= 8000)):
    print('Sua classificação é Platina')
if ((exp >= 8001) and (exp <= 9000)):
    print('Sua classificação é Ascendente')
if ((exp >= 9001) and (exp <= 10000)):
    print('Sua classificação é Imortal')
if exp >= 10001:
    print('Sua classificação é Radiante')