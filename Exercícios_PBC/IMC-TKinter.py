import tkinter as tk

#Criando Janela
root = tk.Tk()
root.title('')

#Configurando Linhas e Colunas
root.rowconfigure(0, weight=1)
root.columnconfigure([0, 1], weight=1)

#Título da Página
titulo = tk.Label(text='Calculador de IMC', bg='#696969')
titulo.grid(row=0, columnspan=2, sticky='EW')

#Configuração das entradas
def testVal(inStr,acttyp):
    if acttyp == '1':
        if not inStr.isdigit():
            return False
    return True

#Entrada de Peso
enter_peso = tk.Label(text=f'{"Peso(gramas):":>25}')
enter_peso.grid(row=1, column=0)

peso = tk.Entry(root, validate="key")
peso['validatecommand'] = (peso.register(testVal),'%P','%d')
peso.grid(row=1, column=1)


#Entrada de Altura
enter_altura = tk.Label(text=f'{"Altura(centímetros):":>21}')
enter_altura.grid(row=2, column=0)

altura = tk.Entry(root, validate="key")
altura['validatecommand'] = (peso.register(testVal),'%P','%d')
altura.grid(row=2, column=1)

#Ações Executadas pelo Botão
def cal_IMC():
    #Calculo d IMC
    val_peso = float(peso.get())
    val_altura = float(altura.get())
    IMC = (val_peso/1000)/((val_altura/100)**2)

    #Impressão do IMC no Página
    r_IMC = tk.Label(text=f'{IMC:.2f}', bg='#C0C0C0', width=17)
    r_IMC.grid(row=4, column=1)

    tx_IMC = tk.Label(text=f'{"IMC:":>32}')
    tx_IMC.grid(row=4, column=0)


    #Classificação do IMC
    clasf = 'Abaixo do Peso'
    if IMC >= 18.5:
        clasf = 'Peso Normal'

    if IMC >= 25:
        clasf = 'Sobrepeso'

    if IMC >= 30:
        clasf = 'Obesidade Grau I'

    if IMC >= 35:
        clasf = 'Obesidade Grau II'

    if IMC >= 40:
        clasf = 'Obesidade Grau III'

    #Impressão da Classificação do IMC no página
    r_IMC = tk.Label(text=clasf, bg='#1C1C1C', fg='white', width=17)
    r_IMC.grid(row=5, column=1)

    tabl = tk.Label(text=f'{"Classificação:":>27}', bg='black', fg='white')
    tabl.grid(row=5, column=0)

#Colocando Botão na Página
botao = tk.Button(text='CALCULAR', command = cal_IMC, bg='#363636', fg='white')
botao.grid(row=3, columnspan=2)

#Start da Página
root.mainloop()
