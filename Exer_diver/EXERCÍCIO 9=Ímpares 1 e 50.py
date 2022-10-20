"""Ímpares 1 e 50
    Por: Ricardo Reis.
       Python 3.9"""

#Cores
limp='\033[m'
az='\033[1;34m'


#Apresentação
print(f"""{az}Números ímpares de 1 a 50: {limp}""" )

#Programa
f=0
for f in range(1,51):
    if f % 2 != 0:
        print(str(f)+',',end=' ')

print('\n',end='')
print('_'*95)