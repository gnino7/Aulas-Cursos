heroi = input('Digite o nome do heroi: ')
print('Olá, ' + heroi)
exp = int(input('Digite o numero de vitorias acumulado: '))
if exp <= 10:
    print('Sua classificação é Ferro')
if ((exp >= 11) and (exp <= 20)):
    print('Sua classificação é Bronze')
if ((exp >= 21) and (exp<= 50)):
    print('Sua classificação é Prata')
if ((exp >= 51) and (exp <= 80)):
    print('Sua classificação é Ouro')
if ((exp >= 81) and (exp <= 90)):
    print('Sua classificação é Diamante')
if ((exp >= 91) and (exp <= 100)):
    print('Sua classificação é Lendario')
if exp >= 101:
    print('Sua classificação é Imortal')