"""1 até 20
    Por: Ricardo Reis.
       Python 3.9"""

#Cores
limp='\033[m'
az='\033[1;34m'


#Apresentação
print(f"""{az}Números positivos de 1 a 20: {limp}""" )

#Programa
f=0
for f in range(1,21):
    print(str(f)+',',end=' ')

print('\n',end='')
print('_'*80)
