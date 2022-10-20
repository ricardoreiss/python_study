import tkinter as tk

#Data de Hoje
from datetime import date
data = date.today()
data = (str(data).split('-'))
data = '/'.join(data[::-1])


class Application(tk.Frame):
    def __init__(self, master=None, data=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.data = data
        self.produtos = {'descricao':[], 'val_unit':[], 'qtd':[], 'val_total':[]}
        self.valTot = 0
        self.QtdItm = 0
        self.aut = 0
        self.clic = 0
        self.create_widgets()
        self.add_bbtc()

    def add_bbtc(self):
        #Inserindo Valores
        self.desc = (str(self.enter_desc.get())).upper()
        self.val_unit = str(self.enter_valUnit.get())
        if self.val_unit:
            if ',' in self.val_unit:
                self.val_unit = (self.val_unit).replace(',','.')

            if not self.val_unit[0].isalpha():
                self.val_unit = float(self.val_unit)


                self.qtd = self.enter_Qtd.get()
                if self.qtd:
                    self.qtd = int(self.enter_Qtd.get())
                    self.val_tot = self.val_unit * self.qtd

                    #Colocando os Valores dentro da Biblioteca
                    if self.qtd > 0 and self.desc and self.val_unit:
                        self.produtos['descricao'].append(self.desc)
                        self.produtos['val_unit'].append(self.val_unit)
                        self.produtos['qtd'].append(self.qtd)
                        self.produtos['val_total'].append(self.val_tot)

        #Inserir N°
        for c in range(len(self.produtos['descricao'])):
            if c < 23:
                frame = tk.Frame(master=root_principal)
                frame.grid(row=c + 2, column=2)
                self.n_prod = tk.Label(master=frame, text=c + 1, bg='#F5DEB3')
                self.n_prod.pack()

        #Inserir Descrição
        for c in range(len(self.produtos['descricao'])):
            if c < 23:
                frame = tk.Frame(master=root_principal)
                frame.grid(row=c + 2, column=3, sticky='w')
                self.n_prod = tk.Label(master=frame, text=(self.produtos['descricao'][c]), bg='#F5DEB3')
                self.n_prod.pack()

        #Inserir Valor Unitário
        for c in range(len(self.produtos['descricao'])):
            if c < 23:
                frame = tk.Frame(master=root_principal)
                frame.grid(row=c + 2, column=4, sticky='w')
                self.n_prod = tk.Label(master=frame, text=f' R${(self.produtos["val_unit"][c]):.2f}', bg='#F5DEB3')
                self.n_prod.pack()

        #Inserir Quantidade
        for c in range(len(self.produtos['descricao'])):
            if c < 23:
                frame = tk.Frame(master=root_principal)
                frame.grid(row=c + 2, column=5)
                self.n_prod = tk.Label(master=frame, text=self.produtos['qtd'][c], bg='#F5DEB3')
                self.n_prod.pack()

        #Inserir Valor Total do produto
        for c in range(len(self.produtos['descricao'])):
            if c < 23:
                frame = tk.Frame(master=root_principal)
                frame.grid(row=c + 2, column=6, sticky='w')
                self.n_prod = tk.Label(master=frame, text=f' R${(self.produtos["val_total"][c]):.2f}', bg='#F5DEB3')
                self.n_prod.pack()

        #Quardando Valor Total
        self.valTot = sum(self.produtos['val_total'])

        #Quardando Quantidade Total
        self.QtdItm = sum(self.produtos['qtd'])

        #Inserindo Valor Total
        self.label_ValTot = tk.Label(self.master, text=f' Total:R${self.valTot:.2f}', font=('Calibri', 50), bg='red',
                                             fg='white', anchor='w', width=14)
        self.label_ValTot.grid(row=1, rowspan=8, column=0, pady=20, sticky='w')

        #Inserindo Qtd.Itens
        self.label_QtdItm = tk.Label(self.master, text=f' Qtd.Itens:{self.QtdItm}', font=('Calibri', 50), bg='red', fg='white', anchor='w', width=14)
        self.label_QtdItm.grid(row=7, rowspan=8, column=0, sticky='w')

        # Limpando Entradas
        self.enter_desc.delete(0, 'end')
        self.enter_Qtd.delete(0, 'end')
        self.enter_valUnit.delete(0, 'end')

    def criar_notaFiscal(self):
        if self.produtos['descricao']:
            self.clic = self.clic + 1

            #Mostrar e Atualizar Janela da Nota Fiscal
            if self.clic > 1:
                self.root_notaFiscal.destroy()

            #Criando Janela da Nota Fiscal
            self.root_notaFiscal = tk.Tk()
            self.root_notaFiscal.title('Nota-Fiscal')
            self.root_notaFiscal.configure(background='#F5DEB3')

            #Inserindo Título
            self.label_tituloNota = tk.Label(master=self.root_notaFiscal, text='PADARIA FERRAGENS', borderwidth=2, relief='solid', bg='#F5DEB3', font='-weight bold -size 7')
            self.label_tituloNota.grid(column=0, columnspan=5, row=0, padx=2, pady=2)

            #Inserindo Texto Cupom Fiscal
            self.label_textNota = tk.Label(master=self.root_notaFiscal, text='CUPOM FISCAL ELETRÔNICO', font='-weight bold -size 7', bg='#F5DEB3')
            self.label_textNota.grid(column=0, row=1, columnspan=5, sticky='w')

            #Inserindo Data
            self.label_data = tk.Label(master=self.root_notaFiscal, text=f'DATA DA COMPRA:{data}', font='-size 7', bg='#F5DEB3')
            self.label_data.grid(column=0, columnspan=5, row=1, sticky='e')

            #Linha
            self.label_linha = tk.Label(master=self.root_notaFiscal, text=f'{"-"*150}', bg='#F5DEB3', font='-size 5')
            self.label_linha.grid(row=2, column=0, columnspan=5)

            #Inserindo Título Coluna N°
            self.label_hast = tk.Label(master=self.root_notaFiscal, text='#', bg='#F5DEB3')
            self.label_hast.grid(row=3, column=0)

            #Inserindo Título Coluna Descrição
            self.label_titleDescri = tk.Label(master=self.root_notaFiscal, text='DESCRIÇÃO          ', bg='#F5DEB3')
            self.label_titleDescri.grid(row=3, column=1, sticky='w')

            #Inserindo Título Coluna Quantidade
            self.label_titleQtd = tk.Label(master=self.root_notaFiscal, text='QTD', bg='#F5DEB3', anchor=None)
            self.label_titleQtd.grid(row=3, column=2)

            #Inserindo Título Coluna Valor Unitário
            self.label_titleValUnit = tk.Label(master=self.root_notaFiscal, text='VAL.UNIT', bg='#F5DEB3', anchor=None)
            self.label_titleValUnit.grid(row=3, column=3)

            #Inserindo Título Coluna Valor Total
            self.label_titleValTotal = tk.Label(master=self.root_notaFiscal, text='VAL.TOTAL', bg='#F5DEB3')
            self.label_titleValTotal.grid(row=3, column=4, sticky='e')

            # Inserir N°
            for c in range(len(self.produtos['descricao'])):
                if c < 23:
                    frame = tk.Frame(master=self.root_notaFiscal)
                    frame.grid(row=c + 4, column=0)
                    self.n_prod = tk.Label(master=frame, text=c + 1, bg='#F5DEB3')
                    self.n_prod.pack()

            # Inserir Descrição
            for c in range(len(self.produtos['descricao'])):
                if c < 23:
                    frame = tk.Frame(master=self.root_notaFiscal)
                    frame.grid(row=c + 4, column=1, sticky='w')
                    self.n_prod = tk.Label(master=frame, text=(self.produtos['descricao'][c]), bg='#F5DEB3')
                    self.n_prod.pack()

            # Inserir Quantidade
            for c in range(len(self.produtos['descricao'])):
                if c < 23:
                    frame = tk.Frame(master=self.root_notaFiscal)
                    frame.grid(row=c + 4, column=2)
                    self.n_prod = tk.Label(master=frame, text=self.produtos['qtd'][c], bg='#F5DEB3')
                    self.n_prod.pack()

            # Inserir Valor Unitário
            for c in range(len(self.produtos['descricao'])):
                if c < 23:
                    frame = tk.Frame(master=self.root_notaFiscal)
                    frame.grid(row=c + 4, column=3)
                    self.n_prod = tk.Label(master=frame, text=f'{(self.produtos["val_unit"][c]):.2f}', bg='#F5DEB3')
                    self.n_prod.pack()

            # Inserir Valor Total do produto
            for c in range(len(self.produtos['descricao'])):
                if c < 23:
                    frame = tk.Frame(master=self.root_notaFiscal)
                    frame.grid(row=c + 4, column=4)
                    self.n_prod = tk.Label(master=frame, text=f'{(self.produtos["val_total"][c]):.2f}', bg='#F5DEB3')
                    self.n_prod.pack()

            #Linha
            self.label_linha = tk.Label(master=self.root_notaFiscal, text=f'{"-" * 150}', bg='#F5DEB3', font='-size 5')
            self.label_linha.grid(row=(len(self.produtos['descricao'])) + 5, column=0, columnspan=5)

            #Inserindo Total
            self.label_textTotal = tk.Label(master=self.root_notaFiscal, text='TOTAL:', font='-weight bold -size 10', bg='#F5DEB3')
            self.label_textTotal.grid(column=0, row=(len(self.produtos['descricao'])) + 6, columnspan=5, sticky='w')

            self.label_valTotal = tk.Label(master=self.root_notaFiscal, text=f'R${self.valTot:.2f}', font='-size 10', bg='#F5DEB3')
            self.label_valTotal.grid(column=0, columnspan=5, row=(len(self.produtos['descricao'])) + 6, sticky='e')

    def restart(self):
        if self.clic > 1:
            self.root_notaFiscal.destroy()

        self.produtos = {'descricao': [], 'val_unit': [], 'qtd': [], 'val_total': []}
        self.add_bbtc()
        # Espaço
        self.espaco0 = tk.LabelFrame(self.master, text=' fewf')
        for j in range(23):
            frame = tk.Frame(master=root_principal)
            frame.grid(row=j + 2, column=2, columnspan=7, sticky='nswe')
            label = tk.Label(master=frame, bg='#F5DEB3', width=120)
            label.pack()

    def create_widgets(self):

        #Título
        self.label_titulo = tk.Label(self.master, text='Padaria Ferragens', font=('Calibri', 40), bg='#5B9BD5', anchor='w')
        self.label_titulo.grid(row=0, column=0, columnspan=7, sticky='nswe')

        #Data de Hoje
        self.label_datahoje = tk.Label(self.master, text=f'Data: {data} ', font=('Calibri', 20),bg='#5B9BD5', anchor='e', width=16)
        self.label_datahoje.grid(row=0, column=5, columnspan=25, sticky='nswe')

        #Espaço
        self.espaco0 = tk.LabelFrame(self.master, text=' fewf')
        for j in range(10):
            frame = tk.Frame(master=root_principal)
            frame.grid(row=j+14, column=0, columnspan=None)
            label = tk.Label(master=frame, text=' ')
            label.pack()

        #Botão Limpar
        self.botao_limpar = tk.Button(self.master, text='Limpar', font=('Calibri', 25), bg='red', command=self.restart)
        self.botao_limpar.grid(row=17, rowspan=7, pady=30, padx=30)

        #Botão Nota Fiscal
        self.botao_nota = tk.Button(self.master, text='Gerar Nota Fiscal', font=('Calibri', 30), bg='#4472C4', command=self.criar_notaFiscal)
        self.botao_nota.grid(rowspan=12, column=0, pady=30 , padx=30)

        #Espaço
        self.espaco = tk.Label(self.master, text='     ')
        self.espaco.grid(row=1, column=1)

        # Espaço
        self.espaco0 = tk.LabelFrame(self.master, text=' fewf')
        for j in range(23):
            frame = tk.Frame(master=root_principal)
            frame.grid(row=j + 2, column=2, columnspan=7, sticky='nswe')
            label = tk.Label(master=frame, bg='#F5DEB3', width=120)
            label.pack()

        #Coluna N°
        self.nmr_itm = tk.Label(self.master, text='N°', font=('Calibri', 20), bg='#4472C4', width=2)
        self.nmr_itm.grid(row=1, column=2, pady=10)

        #Coluna Descrição
        self.descricao_itm = tk.Label(self.master, text='Descrição', font=('Calibri', 20), bg='#4472C4', width=34, anchor='w')
        self.descricao_itm.grid(row=1, column=3, pady=10, padx=1)

        #Coluna Val.Unit
        self.valUnit_itm = tk.Label(self.master, text='Val.Unit', font=('Calibri', 20), bg='#4472C4', width=8)
        self.valUnit_itm.grid(row=1, column=4, pady=10)

        #Coluna Qtd
        self.Qtd_itm = tk.Label(self.master, text='Qtd', font=('Calibri', 20), bg='#4472C4', width=5)
        self.Qtd_itm.grid(row=1, column=5, pady=10, padx=1)

        #Coluna Val.Total
        self.valTotal_itm = tk.Label(self.master, text='Val.Total', font=('Calibri', 20), bg='#4472C4', width=9)
        self.valTotal_itm.grid(row=1, column=6, pady=10)

        #ADD Produto

        self.background = tk.Label(self.master, bg='#4472C4', font=('Calibri', 20), width=60)
        self.background.grid(row=25, column=2, columnspan=5, rowspan=3, sticky='sn')

        def testVal(inStr, acttyp):
            if acttyp == '1':
                if not inStr.isdigit():
                    return False
            return True

        #Descrição
        self.descricao_itm = tk.Label(self.master, text='Descrição', font=('Calibri', 20), bg='#4472C4', width=36, anchor='w')
        self.descricao_itm.grid(row=25, column=2, columnspan=2)

        self.enter_desc = tk.Entry(self.master, font=('Calibri', 20), width=36)
        self.enter_desc.grid(row=26, column=2, columnspan=2)

        #Val.Unit
        self.valUnit_itm = tk.Label(self.master, text='Val.Unit', font=('Calibri', 20), bg='#4472C4', width=8)
        self.valUnit_itm.grid(row=25, column=4)

        self.real = tk.Label(self.master, text='R$', font=('Calibri', 19), bg='#4472C4')
        self.real.grid(row=26, column=4, sticky='w')

        self.enter_valUnit = tk.Entry(self.master, font=('Calibri', 20), width=6)
        self.enter_valUnit.grid(row=26, column=4, sticky='e')

        #Qtd
        self.Qtd_itm = tk.Label(self.master, text='Qtd', font=('Calibri', 20), bg='#4472C4', width=5)
        self.Qtd_itm.grid(row=25, column=5)

        self.enter_Qtd = tk.Entry(self.master, font=('Calibri', 20), width=4, validate="key")
        self.enter_Qtd['validatecommand'] = (self.enter_Qtd.register(testVal),'%P','%d')
        self.enter_Qtd.grid(row=26, column=5)

        # Botão Adicionar Produto
        self.botao_addprod = tk.Button(self.master, text='Adicionar\nProduto', font=('Calibri', 15), command=self.add_bbtc)
        self.botao_addprod.grid(row=25, rowspan=2, column=6, pady=7)

#Start da Janela
root_principal = tk.Tk()
root_principal.title('Point-of-Sale')
root_principal.state('zoomed')
app = Application(master=root_principal, data=data)
app.mainloop()

