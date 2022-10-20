"""    Palíndromo
    Por: Ricardo Reis.
       Python 3.9"""
from unidecode import unidecode

#Cores
limp='\033[m'
az='\033[1;34m'

#Inserção de Texto
txt_o = input(str(f'{az}Insira um texto:{limp}')).strip()
txt = txt_o.replace(' ','')
txt = txt.replace('.','')
txt = txt.replace(',','')
txt = txt.replace(';','')
txt = unidecode(txt)

#Invertendo texto
txt_i = txt[::-1]

#Confirmando Políndromo
c = ''
if txt != txt_i:
    c='não '

#Resposta
print(f'{az}"{txt_o}" {c}é um POLÍNDROMO.')
