""""Turnos
    Por: Ricardo Reis."""

#Cores
limp='\033[m'
az='\033[1;34m'
ama='\033[1;33m'
verm='\033[1;31m'
verd='\033[1;32m'
rox='\033[1;35m'

#Apresentação
nome=str(input(f'{az}Qual é o seu nome?{limp}')).strip().capitalize()
print(f"""{az}Em que turno você estuda?{limp}
{rox}[M]Matutino
[V]Vespertino
[N]Noturno{limp}
""",'_'*30)

#Programação
s=str(input(f'{az}Opção:{limp}')).strip().lower()

if s in 'mvn':
    #Status
    if s=='m':
        s1=f'{ama}Bom dia!!!{limp}'
    elif s=='v':
        s1 = f'{verd}Boa tarde!!!{limp}'
    elif s=='n':
        s1 = f'{rox}Boa noite!!!{limp}'

    print(f'{s1} {nome}.')
else:
    print(f'{verm}Opção inválida.{limp}')

