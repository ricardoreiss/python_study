"""Taxas Full
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
print(f"""{az}Insira o número de habitantes e a taxa percentual de crescimento de cada país. {limp}""" )
print('_'*80)

#Validação dos valores
f=0
a=int(input(f'{az}População do País1:'))
at=float(input(f'{az}Taxa percentual de crescimento do país1:'))
b=int(input(f'{az}População do País2:'))
bt=float(input(f'{az}Taxa percentual de crescimento do país2:{limp}'))
print('_'*80)

lis=[a,b]
lis4=sorted(lis)
z=1

#Programação
if a==b:
    if at==bt:
        print(f'{verd}País1 e País2 sempre terão os mesmo número de habitantes, conforme as taxas de crescimento.{limp}')
        quit()

    else:
        lis1=[at,bt]
        lis2=sorted(lis1)
        pma=(lis1.index(lis2[1]))+1
        pme=(lis1.index(lis2[0]))+1
        z=0

if a>b and at>=bt:
    pma = '1'
    pme = '2'
    z=0

if b>a and bt>=at:
    pma = '2'
    pme = '1'
    z=0

if z==0:
    print(f'{verd}O número de habitantes do País{pma} sempre será maior que o do País{pme}, conforme as taxas de crescimento.{limp}')
    quit()

b=lis4[0]
a=lis4[1]
while a>b:
    lis3 = [at, bt]
    at1=(lis.index(lis4[1]))
    bt1=(lis.index(lis4[0]))

    a=a+((a/100)*lis3[at1])
    b=b+((b/100)*lis3[bt1])
    f=f+1

print(f'{az}Daqui a {verd}{f} anos {az}o {rox}País {bt1+1} {az}tera mais habitantes que o {rox}País {at1+1}{az}, conforme as taxas de crescimento.{limp}')
