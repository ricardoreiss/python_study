"""Jogo de Craps
    Por: Ricardo Reis.
       Python 3.9"""

#Cores
limp='\033[m'
az='\033[1;34m'
ama='\033[1;33m'
verm='\033[1;31m'
rox='\033[1;35m'
verd='\033[1;32m'

from random import randint

#Apresentação
print(f"""{verm}       _________________
       I {limp}JOGO DE CRAPS{verm} I
       I_______________I{limp}""")

input(f'Aperte {az}ENTER{limp} para os jogar dados.')

#Função que imprime o formato do dados
def dados(n):
    print(' ')
    print(end='')
    if n==1:
        print("""            [     ]
            [  0  ]
            [     ]""")
    if n==2:
        print("""            [0    ]
            [     ]
            [    0]""")
    if n==3:
        print("""            [0    ]
            [  0  ]
            [    0]""")
    if n==4:
        print("""            [0   0]
            [     ]
            [0   0]""")
    if n==5:
        print("""            [0   0]
            [  0  ]
            [0   0]""")
    if n==6:
        print("""            [0   0]
            [0   0]
            [0   0]""")

#Impressão e sorteio de dados
print(verm+'-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'+az)

d1=randint(1,6)
d2=randint(1,6)
t=d1+d2

dados(d1)
dados(d2)

print('Total:' + str(t))
print(verm + '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-' + az)

#Formulação e impressão dos resultados
if t==7 or t==11:
    print(verd+'           +NATURAL+')
    print('        !!!VC GANHOU!!!')
elif t==2 or t==3 or t==12:
    print(verm+'           -CRAPS-')
    print('          VC PERDEU')

else:
    #Repetição caso tenha pontos
    t1=0
    while t1 != t and t1 != 7:
        print(ama+'IIIHHH. Você terá que jogar novamente. BOA SORTE!')
        input(f'   Aperte {az}ENTER {ama}para continuar.')

        print(verm + '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-' + az)

        d1 = randint(1, 6)
        d2 = randint(1, 6)
        t1 = d1 + d2

        dados(d1)
        dados(d2)

        print('Total:' + str(t1))
        print(verm + '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-' + az)

    if t1 == t:
        print(verd + '           +NATURAL+')
        print('        !!!VC GANHOU!!!')

    elif t1 == 7:
        print(verm + '           -CRAPS-')
        print('          VC PERDEU')
