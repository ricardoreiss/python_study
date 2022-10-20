
from random import randint

m=randint(1,10)
s='i'
ir=pr='\033[1;31mPERDEU\033[m'
v='\033[1;33mGANHOU\033[m'
while s in 'ip':
    s=str(input('Ímpar(i) ou Par(p)?')).strip().lower()
    if s in 'ip':
        if s=='i':
            ir=v
        if s=='p':
            pr=v

        n=int(input('Qual é o seu valor?'))
        if (m+n)%2==0:
            print(f'Eu escolhi \033[1;34m{m}\033[m você {pr}.')
        else:
            print(f'Eu escolhi \033[1;34m{m}\033[m você {ir}.')

    print('_'*30)