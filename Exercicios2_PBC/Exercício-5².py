
#Inserção e Formatação de Valores
d=input('\033[1;34mInsira uma data válida [DD/MM/AAAA]:')
d=d.split('/')

#Lista Composta pelos Meses
m=['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

#Impressão e Formatação da Data
print(f'Data Formatada:Dia {d[0]} de {m[int(d[1])-1]}, de {d[2]}.')

