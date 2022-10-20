import tkinter as tk
from tkinter import ttk
from random import choice

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.itens = []
        self.cores = ['RED', 'GREEN', 'BLUE', 'YELLOW', 'PURPLE', 'PINK', 'ORANGE', 'GRAY', 'WHITE']
        self.tf_butadd = 0
        self.tf_aviso1 = 0
        self.tf_aviso2 = 0
        self.tf_aviso3 = 0
        self._adicionar()
        self.add_lista()
        self.espaco_pilha()
        self.remover()

#Comandos
    def pilha(self):
        for c in range(len(self.itens)):
            if c < 7:
                self.iit = str(self.itens[c]).split('-')
                frame = tk.Frame(master=self.master)
                frame.grid(row=7 - c, column=4, sticky='ns')
                self.n_prod = tk.Label(master=frame, text=self.iit[0:-1], bg=self.iit[-1], font=('Calibri', 10), borderwidth = 2,
         relief='ridge')
                self.n_prod.pack()


    def add_lista(self):
        self.tf_butadd += 1
        self.it = self.enter_item.get()

        if self.it and len(self.it) <= 30:
            if self.tf_aviso1 == 1:
                self.aviso1.destroy()
                self.tf_aviso1 = 0

            if not len(self.itens) > 6:
                self.itens.append((self.enter_item.get())+'-'+choice(self.cores))

            self.pilha()

        else:
            if self.tf_butadd > 2:
                if self.tf_aviso3 == 0:
                    if self.tf_aviso1 == 0:
                        self.aviso1 = tk.Label(self.master, text='*Insira um valor com no máximo 30 caractêres*', fg='red')
                        self.aviso1.grid(column=1, columnspan=2, row=4)
                        self.tf_aviso1 = 1

                else:
                    self.aviso3.destroy()

                self.enter_itempararmv.destroy()


        if len(self.itens) > 6:
            self.aviso3 = tk.Label(self.master, text='*Você atingiu o máximo de itens(7)*', fg='red')
            self.aviso3.grid(column=1, columnspan=2, row=4)
            self.tf_aviso3 = 1

        self.enter_itempararmv = ttk.Combobox(self.master, values=self.itens, font=('Calibri', 10), width=28)
        self.enter_itempararmv.grid(row=6, column=1, pady=5, rowspan=2)

        self.enter_item.delete(0,'end')

    def remover_lista(self):
        self.itrmv = self.enter_itempararmv.get()
        if self.tf_aviso2 == 1:
            self.aviso2.destroy()

        if self.itrmv and (self.itrmv in self.itens):
            self.itens.remove(self.itrmv)

            self.enter_itempararmv.destroy()
            self.enter_itempararmv = ttk.Combobox(self.master, values=self.itens, font=('Calibri', 10), width=28)
            self.enter_itempararmv.grid(row=6, column=1, pady=5, rowspan=2)

            for c in range(8):
                frame = tk.Frame(master=self.master)
                frame.grid(row=c, column=4, sticky='ns')
                self.n_prod = tk.Label(master=frame, font=('Calibri', 10), bg='#FFE699', width=30)
                self.n_prod.pack()

            self.pilha()

            if len(self.itens) <= 6 and self.tf_aviso3 == 1:
                self.espaco = tk.Label(self.master, font=('Calibri', 10), width=30)
                self.espaco.grid(row=4, column=1, columnspan=2)
                self.tf_aviso3 = 0

        else:
            self.aviso2 = tk.Label(self.master, text='*Insira um item que esteja na pilha*', fg='red')
            self.aviso2.grid(column=1, columnspan=2, row=8)
            self.tf_aviso2 = 1

        self.enter_itempararmv.delete(0,'end')

#Programa
    def _adicionar(self):

        self.espaco = tk.Label(self.master, text=' ', font=('Calibri', 5))
        self.espaco.grid(row=0, column=0, columnspan=2)

        self.espaco = tk.Label(self.master, text=' ', font=('Calibri', 5))
        self.espaco.grid(row=0, column=0)

        self.add_title = tk.Label(self.master, text='Adicionar Item na Pilha', font=('Calibri', 10), bg='#4472C4', width=40, borderwidth=1, relief='solid')
        self.add_title.grid(row=1, column=1, columnspan=2)

        self.enter_item = tk.Entry(self.master, font=('Calibri', 10), width=30)
        self.enter_item.grid(row=2, column=1, pady=5, rowspan=2)

        self.botao_adicionar = tk.Button(self.master, text='Adicionar', font=('Calibri', 10), bg='green', width=7, command=self.add_lista)
        self.botao_adicionar.grid(row=2, column=2, pady=5, rowspan=2)

    def remover(self):

        self.rmv_title = tk.Label(self.master, text='Remover Item da Pilha', font=('Calibri', 10), bg='#4472C4', width=40, borderwidth=1, relief='solid')
        self.rmv_title.grid(row=5, column=1, columnspan=2)

        self.botao_rmv = tk.Button(self.master, text='Remover', font=('Calibri', 10), bg='red', width=7, command=self.remover_lista)
        self.botao_rmv.grid(row=6, column=2, pady=5, rowspan=2)

        self.espaco = tk.Label(self.master, text=' ', font=('Calibri', 5))
        self.espaco.grid(row=0, column=3)


    def espaco_pilha(self):
        for c in range(8):
            frame = tk.Frame(master=self.master)
            frame.grid(row=c, column=4, sticky='ns')
            self.n_prod = tk.Label(master=frame, font=('Calibri', 10), bg='#FFE699', width=30)
            self.n_prod.pack()

#Start da Janela
root = tk.Tk()
root.title('Pilha')
app = Application(master=root)
app.mainloop()