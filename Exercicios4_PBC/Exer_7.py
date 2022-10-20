"""Quantidade de Espaços e Vogais
        Por: Ricardo Reis.
           Python 3.9"""

#Cores
limp='\033[m'
az='\033[1;34m'

#Inserção do Texto
txt = input(str(f'{az}Insira um texto:{limp}')).strip()

#Quantidade de Espaços
print(f'{az}Quantidade de espaços em "{txt}":{limp}{txt.count(" ")}')

#Quantidade de Vogais
v=0
for c in ['a','e','i','o','u']:
    v=v+txt.count(c)

print(f'{az}Quantidade de vogais em "{txt}":{limp}{v}')