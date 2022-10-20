
n=str(input('Insira um número:')).strip()

if str(n.isnumeric()) == 'True':
    n=n[::-1]+'0000'

    print('Unidades:{}' .format(n[0]))
    print('Dezenas:{}' .format(n[1]))
    print('Centenas:{}' .format(n[2]))
    print('Milhares:{}' .format(n[3]))
    print('Dezenas de milhares:{}' .format(n[4]))

else:
    print('Reinicie o programa e insira um valor numérico.')