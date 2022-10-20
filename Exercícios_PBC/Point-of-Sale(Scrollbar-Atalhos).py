import tkinter as tk
from tkinter import *
from tkinter import ttk

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
        self.produtos = []
        self.valTot = 0
        self.QtdItm = 0
        self.aut = 0
        self.clic = ''
        self.posi_desc = 0
        self.posi_valUnit = 1
        self.posi_qtd = 2
        self.posi_valTot = 3
        self.travel_selecao = ''
        self.values = ''
        self.travel_tabel = ''
        self.point_click = ''
        self.enter_foc = ''
        self.d_f =[]
        self.travel_ValQtd = []
        self.create_widgets()
        self.add_bbtc()


    def clean_ent(self):
        self.enter_desc.delete(0, 'end')
        self.enter_Qtd.delete(0, 'end')
        self.enter_valUnit.delete(0, 'end')

    def tabel(self):
        if self.travel_tabel:
            self.my_tree.destroy()

        style = ttk.Style()
        style.theme_use("alt")
        # Pick a theme
        style.configure("Treeview", background="#F5DEB3", fieldbackground="#F5DEB3")
        style.configure('Treeview.Heading', background='#4472C4', foreground="black", font=('Calibri', 20))

        # Change selected color
        style.map('Treeview', background=[('selected', 'blue')])

        # Create Treeview Frame
        tree_frame = Frame(root_principal)
        tree_frame.grid(row=1, rowspan=29, column=2, columnspan=5, sticky='n', pady=5)

        # Treeview Scrollbar
        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        # Create Treeview
        self.my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, height=25)
        # Pack to the screen
        self.my_tree.pack()

        # Configure the scrollbar
        tree_scroll.config(command=self.my_tree.yview)

        # Define Our Columns
        self.my_tree['columns'] = ("N°", "Desc", "ValUnit", "Qtd", "ValTot")

        # Formate Our Columns
        self.my_tree.column("#0", width=0, stretch=NO)
        self.my_tree.column("N°", anchor=CENTER, width=50)
        self.my_tree.column("Desc", anchor=W, width=400)
        self.my_tree.column("ValUnit", anchor=W, width=150)
        self.my_tree.column("Qtd", anchor=CENTER, width=75)
        self.my_tree.column("ValTot", anchor=W, width=150)

        # Create Headings
        self.my_tree.heading("#0", text="", anchor=W)
        self.my_tree.heading("N°", text="N°", anchor=CENTER)
        self.my_tree.heading("Desc", text="Descrição", anchor=W)
        self.my_tree.heading("ValUnit", text="Val.Unit", anchor=CENTER)
        self.my_tree.heading("Qtd", text="Qtd", anchor=CENTER)
        self.my_tree.heading("ValTot", text="Val.Total", anchor=CENTER)

        for record in range(len(self.produtos)):
            self.my_tree.insert(
                parent='', index='end', text="", values=(record+1, (self.produtos[record])[0], f'R${(self.produtos[record])[1]:.2f}', (self.produtos[record])[2], f'R${(self.produtos[record])[3]:.2f}'))

        self.travel_tabel = 1

    def chamado_add(self,e):
        self.entrada_op = str(root_principal.focus_get())
        if self.entrada_op == '.':
            self.enter_foc = self.enter_desc

        elif self.entrada_op == '.!entry':
            self.enter_foc = self.enter_valUnit

        elif self.entrada_op == '.!entry2':
            self.enter_foc = self.enter_Qtd

        elif self.entrada_op == '.!entry3':
            self.enter_foc = self.enter_desc
            self.add_bbtc()

        self.enter_foc.focus_set()

    def voltar_entrada(self,e):
        self.entrada_op = str(root_principal.focus_get())
        if '.!entry' in self.entrada_op:

            if self.entrada_op == '.!entry2':
                self.enter_foc = self.enter_desc

            elif self.entrada_op == '.!entry3':
                self.enter_foc = self.enter_valUnit

            if self.enter_foc:
                self.enter_foc.focus_set()

    def avancar_entrada(self,e):
        self.entrada_op = str(root_principal.focus_get())
        if '.!entry' in self.entrada_op:

            if self.entrada_op == '.!entry':
                self.enter_foc = self.enter_valUnit

            elif self.entrada_op == '.!entry2':
                self.enter_foc = self.enter_Qtd

            if self.enter_foc:
                self.enter_foc.focus_set()

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
                        self.produtos.append([self.desc, self.val_unit, self.qtd, self.val_tot])

        #Quardando Valor Total
        self.valTot = 0
        for c in self.produtos:
            self.valTot += c[self.posi_valTot]

        #Quardando Quantidade Total
        self.QtdItm = 0
        for c in self.produtos:
            self.QtdItm += c[self.posi_qtd]

        #Inserido Vals Tot Qtd
        if self.travel_ValQtd:
            self.label_ValTot.destroy()
            self.label_QtdItm.destroy()

        #Inserindo Valor Total
        self.label_ValTot = tk.Label(self.master, text=f' Total:R${self.valTot:.2f}', font=('Calibri', 50), bg='red', fg='white', anchor='w', width=14)
        self.label_ValTot.grid(row=1, rowspan=8, column=0, pady=20, sticky='w')

        #Inserindo Qtd.Itens

        self.label_QtdItm = tk.Label(self.master, text=f' Qtd.Itens:{self.QtdItm}', font=('Calibri', 50), bg='red', fg='white', anchor='w', width=14)
        self.label_QtdItm.grid(row=7, rowspan=8, column=0, sticky='w')

        self.travel_ValQtd = 1

        # Limpando Entradas
        self.clean_ent()

        #Colocando Tabela
        self.tabel()



    def chamado_nota(self,e):
        self.criar_notaFiscal()

    def criar_notaFiscal(self):
        if self.clic:
            self.root_notaFiscal.destroy()

        if self.produtos:

            #Mostrar e Atualizar Janela da Nota Fiscal
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
            for c in range(len(self.produtos)):
                if c < 23:
                    frame = tk.Frame(master=self.root_notaFiscal)
                    frame.grid(row=c + 4, column=0)
                    self.n_prod = tk.Label(master=frame, text=c + 1, bg='#F5DEB3')
                    self.n_prod.pack()

            # Inserir Descrição
            for c in range(len(self.produtos)):
                if c < 23:
                    frame = tk.Frame(master=self.root_notaFiscal)
                    frame.grid(row=c + 4, column=1, sticky='w')
                    self.n_prod = tk.Label(master=frame, text=((self.produtos[c])[self.posi_desc]), bg='#F5DEB3')
                    self.n_prod.pack()

            # Inserir Quantidade
            for c in range(len(self.produtos)):
                if c < 23:
                    frame = tk.Frame(master=self.root_notaFiscal)
                    frame.grid(row=c + 4, column=2)
                    self.n_prod = tk.Label(master=frame, text=((self.produtos[c])[self.posi_qtd]), bg='#F5DEB3')
                    self.n_prod.pack()

            # Inserir Valor Unitário
            for c in range(len(self.produtos)):
                if c < 23:
                    frame = tk.Frame(master=self.root_notaFiscal)
                    frame.grid(row=c + 4, column=3)
                    self.n_prod = tk.Label(master=frame, text=f'{((self.produtos[c])[self.posi_valUnit]):.2f}', bg='#F5DEB3')
                    self.n_prod.pack()

            # Inserir Valor Total do produto
            for c in range(len(self.produtos)):
                if c < 23:
                    frame = tk.Frame(master=self.root_notaFiscal)
                    frame.grid(row=c + 4, column=4)
                    self.n_prod = tk.Label(master=frame, text=f'{((self.produtos[c])[self.posi_valTot]):.2f}', bg='#F5DEB3')
                    self.n_prod.pack()

            #Linha
            self.label_linha = tk.Label(master=self.root_notaFiscal, text=f'{"-" * 150}', bg='#F5DEB3', font='-size 5')
            self.label_linha.grid(row=(len(self.produtos)) + 5, column=0, columnspan=5)

            #Inserindo Total
            self.label_textTotal = tk.Label(master=self.root_notaFiscal, text='TOTAL:', font='-weight bold -size 10', bg='#F5DEB3')
            self.label_textTotal.grid(column=0, row=(len(self.produtos)) + 6, columnspan=5, sticky='w')

            self.label_valTotal = tk.Label(master=self.root_notaFiscal, text=f'R${self.valTot:.2f}', font='-size 10', bg='#F5DEB3')
            self.label_valTotal.grid(column=0, columnspan=5, row=(len(self.produtos)) + 6, sticky='e')

            self.clic = 1
            self.root_notaFiscal.protocol("WM_DELETE_WINDOW", self.janela_end)
            self.root_notaFiscal.bind('<Escape>', self.chamado_jaend)
            root_principal.bind('<Escape>', self.chamado_jaend)

    def chamado_jaend(self,e):
        self.janela_end()

    def janela_end(self):
        self.root_notaFiscal.destroy()
        self.clic = ''

    def chamado_restart(self,e):
        self.restart()

    def restart(self):

        self.produtos = []
        self.add_bbtc()

        # Espaço
        for record in self.my_tree.get_children():
            self.my_tree.delete(record)

    def chamado_deletar(self,e):
        if '.!treeview' in str(root_principal.focus_get()):
            self.deletar_prod()

    def deletar_prod(self):
        if self.values:
            self.clean_ent()
            self.prod = self.my_tree.selection()[0]
            self.my_tree.delete(self.prod)

            posi_values = self.produtos.index(self.values)
            self.produtos.pop(posi_values)

            self.add_bbtc()

    def select_record(self,e):
        # Clear entry boxes
        self.clean_ent()

        # Grab record number
        selected = self.my_tree.focus()
        # Grab record values
        self.values = self.my_tree.item(selected, 'values')
        if self.values:
            self.values = [self.values[1], self.values[2], self.values[3], self.values[4]]
            self.values[1] = float(str(self.values[1]).replace('R$',''))
            self.values[2] = int(self.values[2])
            self.values[3] = float(str(self.values[3]).replace('R$',''))

            # output to entry boxes
            self.enter_desc.insert(0, self.values[0])
            self.enter_valUnit.insert(0, self.values[1])
            self.enter_Qtd.insert(0, self.values[2])

            self.travel_selecao = 1

    def selecao(self,e):

        self.select_record('')
        if not self.values:
            # Já deixar um item selecionado
            list = self.my_tree.get_children()
            if list:
                self.my_tree.selection_set(list[0])
                self.my_tree.focus(list[0])
                self.my_tree.focus_force()

        self.select_record('')

    def travel_d(self,e):
        self.select_record('')

    def not_selec(self,e):
        self.my_tree.bind("<ButtonRelease-1>", self.travel_d)

        if self.travel_selecao and self.point_click == '':
            self.my_tree.selection_set()
            self.my_tree.focus()
            self.my_tree.focus_force()
            self.travel_selecao = ''
            self.point_click = ''
            self.clean_ent()

        self.point_click = ''

    def lista_ata(self,e):
        self.root_listAta = tk.Tk()
        self.root_listAta.title('Lista-de-Atalhos')

        #Lista
        self.atalhos = """Ctrl+Enter: Gerar Nota Fiscal
Delete: Deletar Compra
Backspace: Deletar Produto
Enter: Adicionar Produto
Seta-Baixo e Cima: Selecionar Produto
Esc: Fecha Nota Fiscal
Double_Shift: Tirar Seleção
Ctrl+-Direita e Esquerda: Selecionar Entrada"""

        #Inserindo Lista
        self.label_ata = tk.Label(master=self.root_listAta, text=self.atalhos, anchor=W)
        self.label_ata.pack()

    def create_widgets(self):

        #Título
        self.label_titulo = tk.Label(self.master, text='Padaria Ferragens', font=('Calibri', 40), bg='#5B9BD5', anchor='w')
        self.label_titulo.grid(row=0, column=0, columnspan=7, sticky='nswe')

        #Data de Hoje
        self.label_datahoje = tk.Label(self.master, text=f'Data: {data} ', font=('Calibri', 20),bg='#5B9BD5', anchor='e', width=16)
        self.label_datahoje.grid(row=0, column=5, columnspan=25, sticky='nswe')

        #Lista Atalhos
        self.label_listaatalhos = tk.Label(self.master, text='Acessar Atalhos:Ctrl+Tab', bg='#5B9BD5', anchor='s')
        self.label_listaatalhos.grid(row=0, column=5, columnspan=25, sticky='s')
        root_principal.bind('<Control-Tab>', self.lista_ata)

        #Espaço
        self.espaco0 = tk.LabelFrame(self.master, text=' fewf')
        for j in range(10):
            frame = tk.Frame(master=root_principal)
            frame.grid(row=j+14, column=0, columnspan=None)
            label = tk.Label(master=frame, text=' ')
            label.pack()

        #Botão Limpar
        self.botao_limpar = tk.Button(self.master, text='Deletar Compra', font=('Calibri', 25), bg='red', command=self.restart)
        self.botao_limpar.grid(row=17, rowspan=7, pady=30, padx=30)
        root_principal.bind('<Delete>', self.chamado_restart)

        #Botão Deletar Item
        self.botao_delprod = tk.Button(self.master, text='Deletar Produto', font=('Calibri', 25), bg='red', command=self.deletar_prod)
        self.botao_delprod.grid(row=22, rowspan=5, pady=30, padx=30)
        root_principal.bind('<BackSpace>', self.chamado_deletar)

        #Botão Nota Fiscal
        self.botao_nota = tk.Button(self.master, text='Gerar Nota Fiscal', font=('Calibri', 30), bg='#4472C4', command=self.criar_notaFiscal)
        self.botao_nota.grid(row=26, rowspan=12, column=0, pady=30 , padx=30)
        root_principal.bind('<Control-Return>', self.chamado_nota)

        #Espaço
        self.espaco = tk.Label(self.master, text='     ')
        self.espaco.grid(row=1, rowspan=10, column=1)

        # Espaço
        self.espaco0 = tk.LabelFrame(self.master, text=' fewf')
        for j in range(27):
            frame = tk.Frame(master=root_principal)
            frame.grid(row=j + 2, column=2, columnspan=7, sticky='nswe')
            label = tk.Label(master=frame, width=120)
            label.pack()

        #Espaço entry
        self.background = tk.Label(self.master, bg='#4472C4', font=('Calibri', 20), width=60, height=5)
        self.background.grid(row=26, column=2, columnspan=5, rowspan=19, sticky='sn')

        def testVal(inStr, acttyp):
            if acttyp == '1':
                if not inStr.isdigit():
                    return False
            return True

        #Descrição
        self.descricao_itm = tk.Label(self.master, text='Descrição', font=('Calibri', 20), bg='#4472C4', width=36, anchor='w')
        self.descricao_itm.grid(row=27, column=2, columnspan=2)

        self.enter_desc = tk.Entry(self.master, font=('Calibri', 20), width=36)
        self.enter_desc.grid(row=28, column=2, columnspan=2, padx=5)

        #Val.Unit
        self.valUnit_itm = tk.Label(self.master, text='Val.Unit', font=('Calibri', 20), bg='#4472C4', width=8)
        self.valUnit_itm.grid(row=27, column=4)

        self.real = tk.Label(self.master, text='R$', font=('Calibri', 19), bg='#4472C4')
        self.real.grid(row=28, column=4, sticky='w')

        self.enter_valUnit = tk.Entry(self.master, font=('Calibri', 20), width=6)
        self.enter_valUnit.grid(row=28, column=4, sticky='e')

        #Qtd
        self.Qtd_itm = tk.Label(self.master, text='Qtd', font=('Calibri', 20), bg='#4472C4', width=5)
        self.Qtd_itm.grid(row=27, column=5)

        self.enter_Qtd = tk.Entry(self.master, font=('Calibri', 20), width=4, validate="key")
        self.enter_Qtd['validatecommand'] = (self.enter_Qtd.register(testVal),'%P','%d')
        self.enter_Qtd.grid(row=28, column=5)

        # Botão Adicionar Produto
        self.botao_addprod = tk.Button(self.master, text='Adicionar\nProduto', font=('Calibri', 15), command=self.add_bbtc)
        self.botao_addprod.grid(row=27, rowspan=2, column=6, pady=7)
        root_principal.bind('<Return>', self.chamado_add)
        root_principal.bind('<Control-Left>', self.voltar_entrada)
        root_principal.bind('<Control-Right>', self.avancar_entrada)

        #Setas Selecionar
        root_principal.bind('<Up>', self.selecao)
        root_principal.bind('<Down>', self.selecao)

        root_principal.bind("<ButtonRelease-1>", self.not_selec)
        root_principal.bind('<Shift_L>', self.not_selec)

#Start da Janela
root_principal = tk.Tk()
root_principal.title('Point-of-Sale')
root_principal.state('zoomed')

app = Application(master=root_principal, data=data)
app.mainloop()