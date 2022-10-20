"""Calculador de Média
    Por: Ricardo Reis.
       Python 3.9"""

#Cores
limp='\033[m'
az='\033[1;34m'
ama='\033[1;33m'
verm='\033[1;31m'

#Apresentação
print(f'{az}Insira os valores. Após inserir todas os valores insira "999" para ver resultados.{limp}')
print('_'*30)

#Programa
back='s'

while back=='s':

    # Validação de valores
    lista = list()
    d = ' '
    f = 1
    while d != 999:
        lista.append(d)
        d = float(input(f'{az}Valor{f}:{limp}'))
        f = f + 1
    lista.remove(' ')

    #Média
    print('_'*30)
    m = 0
    for c in lista:
        m = m + int(c)
    m = m / len(lista)

    print('{}Média:{}''{:.1f}' .format(az, limp, m))

    #Soma
    s = 0
    for c in lista:
        s = s + int(c)

    print('{}Soma:{}''{:.1f}'.format(az, limp, s))

    #Maior
    lista=sorted(lista)
    print(f'{az}Maior número:{limp}{lista[-1]}')




    #Restart
    print('_' * 30)
    back = str(input(f'{az}Tentar novamente[s/n]:{limp}')).strip().lower()
    print('_' * 30)