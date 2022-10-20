"""    Strings
    Por: Ricardo Reis.
       Python 3.9"""

#Cores
limp='\033[m'
az='\033[1;34m'

#Inserção de Texto
txt = input(str(f'{az}Insira um texto:{limp}')).upper().strip()
txt = txt.replace(' ','')

#Texto Invertido
print(f'{az}Texto Invertido:{limp}{txt[::-1]}')

#Texto na Vertical
print(f'{az}Texto na Vertical:{limp}')
for l in txt:
    print(l)

#Texto na Vertical em Escada
print(f'{az}Texto na Vertical em Escada:{limp}')
for c in range(len(txt)):
    print(txt[:c+1])

#Texto na Vertical em Escada Invertida
print(f'{az}Texto na Vertical em Escada Invertida:{limp}')
for c in range(len(txt)):
    print(txt[:len(txt)-c])