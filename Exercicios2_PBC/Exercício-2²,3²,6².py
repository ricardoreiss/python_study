"""Contagem Inversão e Embaralho
    Por: Ricardo Reis.
       Python 3.9"""

from random import sample

#Inserção e Formataçõa do Fragmento
n=str(input('\033[1;34mInsira um valor númérico ou palavra:')).strip()

#Contagem de Algarismos do Fragmento
print('\033[1;34mQuantidade de Algarismos:'+'\033[1;31m'+str(len(n)))

#Inversão de Algarismos do Fragmento
print('\033[1;34mFragmento Invertido:'+'\033[1;31m'+n[::-1])

#Embaralho de Algarismos do Fragmento
print('\033[1;34mPalavra Embaralhada:'+'\033[1;31m'+(''.join(sample(n, len(n)))).lower())



