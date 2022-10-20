""""Maior ou Menor
    Por: Ricardo Reis."""

#Cores
limp='\033[m'
az='\033[1;34m'
ama='\033[1;33m'
verm='\033[1;31m'

#Apresentação
print(f'{az}Insira as notas. Após inserir todas as notas insira "p" para ver resultados.{limp}')
print('_'*30)

#Programa
back='s'
while back=='s':
    while back not in 'topn':

        # Validação de notas
        lista = list()
        d = ' '
        f = 1
        while d != 'p':
            lista.append(d)
            d = str(input(f'{az}Valor{f}:{limp}')).strip().lower()
            if str(d.isnumeric()) == 'True':
                d = int(d)

            elif str(d) != 'p':
                back = 'top'
                break
            f = f + 1

        lista.remove(' ')
        if back == 'top':
            print(f'{ama}É validado apenas valores númericos e "p".{limp}')
            break

        #Organização de lista de forma crescente
        print('_'*30)
        lista=sorted(lista)

        # Status
        print(f'{az}Maior número:{limp}{lista[-1]}')
        print(f'{az}Menor número:{limp}{lista[0]}')

        break

    #Restart
    print('_' * 30)
    back = str(input(f'{az}Tentar novamente[s/n]:{limp}')).strip().lower()
    print('_' * 30)