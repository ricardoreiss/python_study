""""Masculino ou Feminino
    Por: Ricardo Reis."""

#Cores
limp='\033[m'
az='\033[1;34m'
ama='\033[1;33m'
verm='\033[1;31m'
verd='\033[1;32m'
rox='\033[1;35m'

#Apresentação
print(f"""{az}Qual o seu sexo?{limp}
{rox}[M]Masculino
[F]Feminino{limp}
""",'_'*30)

#Programação
s=str(input(f'{az}Opção:{limp}')).strip().lower()

if s in 'mf':
    #Status
    if s=='m':
        s1=f'{az}MASCULINO{limp}'
    elif s=='f':
        s1 = f'{verm}FEMININO{limp}'

    print(f'Seu {rox}sexo{limp} é {s1}.')
else:
    print(f'{ama}Sexo inválido.{limp}')

