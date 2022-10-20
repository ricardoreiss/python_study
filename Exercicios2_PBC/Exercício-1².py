"""Prestações e Atrasos
    Por: Ricardo Reis.
       Python 3.9"""

#Cores
limp='\033[m'
az='\033[1;34m'
ama='\033[1;33m'
verm='\033[1;31m'
verd='\033[1;32m'


#Apresentação
print(f'{az}Insira os valores das prestações. Após inserir todas\nas prestações insira "0" para ver o relatório.')
print('_'*52)

#Programação
p=1
n=1
vp=[0]
while p != 0:
    #Inserção dos Valores e Atrasos
    p=float(input(f'{verd}Valor da prestação{n}:R$'))
    n=n+1
    if p != 0:
        at=int(input('Quantidade de dias de atraso:'))
        if at >= 0:
            #Resolução do Total Unitário
            pc=(p/100)
            pt=p + (pc * 3) + (pc * (at / 10))
            vp.append(pt)
            print(ama+'_'*35+limp)
            #Impressão do Total Unitário
            print(f'{verd}Total:R${pt:.2f}{limp}')
            print(az + '_' * 52 + limp)


if n > 2:
    #Valores para Formação do Relatório
        vpm=sorted(vp)
        pm=f'{vpm[-1]:.2f}'
        l=(15+int(len(str(n)))+len(pm)+n-2)
        c=('_'*l)
        t = 0
        stt = 0
    #Resolução e Impressão do Relatório
        print(verm+c)
        r='Relatório:'
        print(f'{r}'+(' '*(l-1-int(len(r))))+'/')
        for c in range(n-2):
            rp=(f' Prestação{c+1}:R${vp[c+1]:.2f}')
            print(rp+(' '*((l-(c+2))-int(len(rp)))+'/'))
            #Formação e Impressão do Total Geral
            t=t+vp[c+1]
            stt=stt+1
        tt=(f' Total:R${t:.2f}')
        print(tt+(' '*((l-(stt+2))-int(len(tt)))+'/'))
        print('_'*(l-(stt+3))+'/')






