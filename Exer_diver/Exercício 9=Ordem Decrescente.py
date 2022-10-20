""""Ordem Decrescente
    Por: Ricardo Reis."""

#Cores
limp='\033[m'
az='\033[1;34m'
ama='\033[1;33m'
verm='\033[1;31m'

#Apresentação
print(f'{az}Insira números nos valores. Após inserir todos os números insira "999" para ver resultados.{limp}')
print('_'*30)

#Programa
# Validação de números
lista = list()
d = ' '
f = 1
while d != 999:
    lista.append(d)
    d = float(input(f'{az}Valor{f}:{limp}'))
    f = f + 1
lista.remove(' ')

#Ordenação
lista1=sorted(lista)
lista2=sorted(lista)[::-1]
print(f'{az}Números em ordem crescente:{limp}{lista1}')
print(f'{az}Números em ordem decrescente:{limp}{lista2}')