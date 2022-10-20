lista={'v':'\033[1;31m',
       'a':'\033[1;34m',
       'l':'\033[m'}

i=int(input('Ano de nascimento:'))
i=2021-i
print('{}Idade:{}{}' .format(lista['a'],lista['l'],i))

if i>18:
    print('Você está {}{} anos{} {}atrasado{} para o alistamento.' .format(lista['a'],abs(18-i),lista['l'],lista['v'],lista['l']))

elif i<18:
    print('Em {}{} anos{} você {}poderá{} se alistar. ' .format(lista['a'],abs(18-i),lista['l'],lista['v'],lista['l']))

elif i==18:
    print('Você já está com a {}idade ideal{} para se alistar.' .format(lista['v'],lista['l']))


