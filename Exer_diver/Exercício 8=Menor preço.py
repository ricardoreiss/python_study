""""Menor preço
    Por: Ricardo Reis."""

#Cores
limp='\033[m'
az='\033[1;34m'
ama='\033[1;33m'
verm='\033[1;31m'

#Apresentação
print(f'{az}Insira o preço dos produtos. Após inserir todos os preços insira  "999" para ver resultados.{limp}')
print('_'*30)

#Programa
back='s'
while back=='s':
    while back not in 'topn':

        # Validação de preços
        lista = list()
        d = ' '
        f = 1
        while d != 999:
            lista.append(d)
            d = float(input(f'{az}Produto{f}:{limp}R$'))
            f = f + 1
        lista.remove(' ')

        #Organização de lista de forma crescente
        print('_'*30)
        lista1=sorted(lista)

        # Status
        print(f'{az}Maior preço:{limp}Produto{(lista.index(lista1[-1]))+1}(R${lista1[-1]:.2f})')
        print(f'{az}Menor preço:{limp}Produto{(lista.index(lista1[0]))+1}(R${lista1[0]:.2f})')
        print('_*30')
        break

    #Restart
    back = str(input(f'{az}Tentar novamente[s/n]:{limp}')).strip().lower()
    print('_' * 30)