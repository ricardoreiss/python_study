"""Tamanho de strings
    Por: Ricardo Reis.
       Python 3.9"""

S1 = input(str('Texto1:')).strip()
S2 = input(str('Texto2:')).strip()
Sts = [S1,S2]

for n in range(2):
    print(f'Tamanho de "{Sts[n]}"= {len(Sts[n])} caracteres.')

if len(S1) == len(S2):
    t='iguais'

else:
    t='diferentes'

if S1 == S2:
    i='iguais'

else:
    i='diferentes'

print(f'As duas strings são de tamanhos {t}.')
print(f'As duas strings tem conteúdos {i}.')