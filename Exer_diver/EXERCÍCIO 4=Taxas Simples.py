"""Taxas Simples
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
print(f"""{az}A população do país A é de 80000 habitantes com uma taxa anual de crescimento de 3% 
e a população do país B é 200000 habitantes com uma taxa de crescimento de 1.5%.{limp}""" )
print('_'*80)

#Programação
f=0
a=80000
b=200000
while a<b:
    a=a+((a/100)*3)
    b=b+((b/100)*1.5)
    f=f+1

print(f'{az}Daqui a {verd}{f} anos {az}o {rox}país A {az}tera mais habitantes que o {rox}país B{az}, conforme as taxas de crescimento.{limp}')