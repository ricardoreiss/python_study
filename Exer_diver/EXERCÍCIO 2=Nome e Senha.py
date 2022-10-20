"""Nome e Senha
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
print(f'{az}Insira seu {rox}Nome de usuário {az}e {rox}Senha{az}.{limp}' )
print('_'*30)

#Valores iniciais
n=0
s=0

#Programação
while n==s:
    n=str(input(f'{az}Nome de usuário:{limp}')).strip().lower()
    s=str(input(f'{az}Senha:{limp}')).strip().lower()

    if n != s:
        print('_'*30)
        print(f'{verd}Valores válidos.{limp}')

    print(f'{verm}Senha inválida.{ama}Insira uma {verm}Senha {ama}diferente do {verm}Nome do usuário{ama}.{limp} ')
    print('_'*30)
