#Conjunto de cores.
cs={'l':'\033[m',
    'a':'\033[1;34m',
    'r':'\033[4;35m'}

#Inserção de notas.
n1=str(input(f'{cs["r"]}Nota1:' .format(cs['r']))).strip()
n2=str(input('Nota2:' .format(cs['r']))).strip()
n3=str(input(f'Nota3:{cs["l"]}' .format(cs['r'],cs['l']))).strip()

#Validação dos valores.
d=3
m1=' '
m2=' '
m3=' '

if str(n1.isnumeric())=='False':
    m1='0'
    d=d-1

if str(n2.isnumeric())=='False':
    m2='0'
    d=d-1

if str(n3.isnumeric())=='False':
    m3='0'
    d=d-1

#Transformação para numérico.
n1=float(str(n1+m1))
n2=float(str(n2+m2))
n3=float(str(n3+m3))

#Média
m=(n1+n2+n3)/d
print(f'{cs["a"]}Média final:{cs["l"]}{m:.1f}')

#Status
if m==10:
    s='Aprovado com distinção'

elif m>=7:
    s='Aprovado'

elif m<7:
    s='Reprovado'

print(f'{cs["a"]}Status:{cs["l"]}{s}')




