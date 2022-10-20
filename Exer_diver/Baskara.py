from sys import exit

a = (input('a:'))
b = (input('b:'))
c = (input('c:'))
print(c.isnumeric())
ct = [a, b, c]
"""for c in range(len(ct)):
    if ct[c] == '':
        ct[c] = 0

    elif ct[c].isnumeric() == False and ct[c].isalnum() == False:

        print('Insira apenas valores numéricos.')
        exit()"""


for c in range(len(ct)):
    ct[c] = float(ct[c])

a = ct[0]
b = ct[1]
c = ct[2]
#Descobrindo Delta
dt = (b) ** 2 - 4 * (a) * (c)
print(dt)

if dt < 0:
    print('Não há RAÍZES reais.')
    exit()
#Resto da Fórmula
dt = (dt) ** 0.5
dts = [+ (dt), - (dt)]

for d in range(len(dts)):
    x = - ((b) + (dts[d])) / (2 * (a))
    print(f'x{d + 1} = {x}')


x1 = (- (b) + (dt)) / (2 * (a))
x2 = (- (b) - (dt)) / (2 * (a))

print(x1)
print(x2)
