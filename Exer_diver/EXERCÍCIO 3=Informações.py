"""Informações
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
print(f'{az}Insira corretamente as informações a seguir.{limp}' )
print('_'*47)

#Programação
br='s'
while br == 's':
    while br == 's':
        n=str(input(f'{az}Nome:')).strip().lower()
        if len(n)<3:
            print(f'{ama}Nome inválido.\nInsira um nome com mais de 3 caracteres.{limp}')
            break

        i=int(input('Idade:'))
        if i<=0 or i>150:
            print(f'{ama}Idade inválida.\nInsira um valor positivo entre 1 e 150.{limp}')
            break

        s=float(input('Salário:R$'))
        if s<=0:
            print(f'{ama}Salário inválido.\nInsira um valor maior que R$0,00.{limp}')
            break

        sx=str(input('Sexo[M/F]:')).strip().lower()
        if sx[0] not in 'mf':
            print(f'{ama}Sexo inválido.\nInsira um sexo válido (M para Masculino e F para Feminino).{limp}')
            break

        ec=str(input(f"""Estado Civil-
{rox}[S]Solteiro(a);
[C]Casado(a);
[V]Viúvo(a);
[D]Divorciado(a).
{az}Opção:{limp}""")).strip().lower()
        if ec[0] not in 'scvd':
            print(f'{ama}Estado Civil inválido.\nInsira um estado civil presente nas opções.{limp}')
            break

        print('_' * 30)
        print(f'{verd}Valores válidos\nObrigado pelas informações.{limp}')
        break

    #Restart
    print('_' * 30)
    br = str(input(f'{az}Tentar novamente[s/n]:{limp}')).strip().lower()
    print('_' * 30)

