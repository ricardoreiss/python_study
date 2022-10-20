"""Zero a Dez
    Por: Ricardo Reis.
       Python 3.9"""

#Cores
limp='\033[m'
az='\033[1;34m'
ama='\033[1;33m'
verm='\033[1;31m'
rox='\033[1;35m'
verd='\033[1;32m'

#Apresentação
print(f'{az}Insira uma nota entre 0 e 10.{limp}')
print('_'*30)

#Programa
n=11
while 0 > n or n > 10:
    n=float(input(f'{az}Nota:{limp}'))

    if 0 <= n <= 10:
        break

    print(f'{ama}O valor da {rox}Nota({n}) {ama}é inválido.{limp}')

print('_'*30)
print(f'{verd}Nota: {n}{limp}')