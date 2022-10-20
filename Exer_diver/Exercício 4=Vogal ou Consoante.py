""""Vogal ou Consoante
    Por: Ricardo Reis."""

#Cores
limp='\033[m'
az='\033[1;34m'
ama='\033[1;33m'
verm='\033[1;31m'
verd='\033[1;32m'
rox='\033[1;35m'

#Apresentação
print(f'{az}Essa letra que você está pensando é vogal ou consoante?{limp}')

#Programação
print('_'*30)
n=str(input(f'{az}Insira essa letra:{limp}')).strip().lower()

if n in 'aeiou':
    s=f'{ama}VOGAL{limp}'
else:
    s=f'{ama}CONSOANTE{limp}'

#Status
print(f'A letra {az}{n}{limp} é {s}.')
print('_'*30)
