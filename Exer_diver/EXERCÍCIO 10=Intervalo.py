"""Intervalo
    Por: Ricardo Reis.
       Python 3.9"""

#Cores
limp='\033[m'
az='\033[1;34m'
verd='\033[1;32m'


#Apresentação
print(f"""{az}Insira números inteiros nas notas. {limp}""" )
print('_'*30)

#Validação
v1=int(input(f'{az}Valor1:'))
v2=int(input(f'Valor2:{limp}'))
print('_'*30)

#Programa
print(f'{az}Os valores inteiros presentes no intervalo entre {v1} e {v2} são-{limp}{verd}')
f=0
if v1 + 1 == v2:
    print('Não há valores inteiros.')


else:
    for f in range(v1+1,v2):
        print(str(f)+',',end=' ')

    print('\n',end='')
print(f'{limp}_'*30)