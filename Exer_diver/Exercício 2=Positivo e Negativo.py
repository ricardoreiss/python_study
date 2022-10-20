""""Positivo ou Negativo
    Por: Ricardo Reis."""

#Cores
limp='\033[m'
az='\033[1;34m'
ama='\033[1;33m'
verm='\033[1;31m'
verd='\033[1;32m'
rox='\033[1;35m'

#Apresentação
print(f'{az}Esse número que você está pensando é positivo ou negativo?{limp}')

#Programação
print('_'*30)
n=int(input(f'{az}Insira esse número:{limp}'))

#Validação
if n>0:
    s=f'{verd}POSITIVO{limp}'
elif n<0:
    s = f'{verm}NEGATIVO{limp}'
elif n==0:
    s = f'{rox}NULO{limp}'

#Status
print(f'O número {az}{n}{limp} é {s}.')
print('_'*30)


