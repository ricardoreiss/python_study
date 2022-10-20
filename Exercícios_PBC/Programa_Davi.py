

class Medico:
    def __init__(self):
        self.nome = input('Nome Completo:')
        self.cpf = int(input('CPF(sem PONTOS e HÍFEM):'))
        self.codigo_credencial = input('Códico de Credêncial:')
        self.campo_atuacao = input('Campo de Atuação:')
        self.hospitais = input('Hospitais de Atuação:')

    def apresentar_cad(self):
        print("\n---------Cadastro---------")
        print("Nome:", self.nome)
        print("CPF:", self.cpf)
        print("Códico de Credêncial:", self.codigo_credencial)
        print("Campo de Atuação:", self.campo_atuacao)
        print("Hospitais de Atuação:", self.hospitais)
        print("--------------------------\n")

    def modificar_cad(self):
        print("CPF:", self.cpf)
        print('Códico de Credêncial:', self.codigo_credencial)
        self.nome = input('Novo Nome Completo:')
        self.campo_atuacao = input('Novo Campo de Atuação:')
        self.hospitais = input('Novo Hospitais de Atuação:')

    def remover_cad(self, lista):
        posicao = lista.index(cad)
        lista.pop(posicao)

class Paciente:
    def __init__(self):
        self.nome = input('Nome Completo:')
        self.idade = input('Idade:')
        self.nascimento = input('Data de Nascimento (dd/mm/aaaa):')
        self.cpf = int(input('CPF(sem PONTOS e HÍFEM):'))
        self.endereco = input('Endereço Completo:')
        self.plano_saude = input('Plano de Saúde:')

    def apresentar_cad(self):
        print("\n---------Cadastro---------")
        print("Nome:", self.nome)
        print("Data de Nascimento:", self.nascimento)
        print("Idade:", self.idade)
        print("CPF:", self.cpf)
        print("Endereço:", self.endereco)
        print("Plano de Saúde:", self.plano_saude)
        print("--------------------------\n")

    def modificar_cad(self):
        print("CPF:", self.cpf)
        self.nome = input('Novo Nome Completo:')
        self.nascimento = input('Nova Data de Nascimento:')
        self.idade = input('Nova Idade:')
        self.endereco = input('Novo Endereço:')
        self.plano_saude = input('Novo Plano de Saúde:')

    def remover_cad(self, lista):
        posicao = lista.index(cad)
        lista.pop(posicao)

def menu_principal():
    print('-' * 50)
    print("1 - Cadastrar")
    print("2 - Apresentar Cadastro")
    print("3 - Modificar Cadastro")
    print("4 - Remover Cadastro")
    print("5 - Sair")
    print('-'*50)
    command = int(input("Digite sua opção:"))

    return command

def menu_secundario():
    print('-'*50)
    print("Na área de...")
    print("1-Cirurgião")
    print("2-Enfermeiro")
    print("3-Paciente")
    print('-' * 50)
    command = int(input("Digite sua opção:"))

    return command

def selecionar():
    command = int(input("CPF do Cadastro:"))

    return command

def procurar(cpf,lista):
    pes = ''
    for cad in lista:
        if cpf == cad.cpf:
            pes = cad
            return pes

    if not pes:
        print('CPF NÃO ENCONTRADO')

list_cirurgiao = []
list_enfermeiro = []
list_paciente = []
listas = [[], list_cirurgiao, list_enfermeiro, list_paciente]
saida = ''
while not saida == 5 and not saida == 'n':
    command = menu_principal()
    saida = command

    #Comandos
    if command != 5:
        command2 = menu_secundario()

        #Cadastrar
        if command == 1:
            if command2 == 1:
                pessoa = Medico()
                list_cirurgiao.append(pessoa)

            elif command2 == 2:
                pessoa = Medico()
                list_enfermeiro.append(pessoa)

            elif command2 == 3:
                pessoa = Paciente()
                list_paciente.append(pessoa)

        #Comandos para Cadastro
        elif command != 1:
            cpf = selecionar()
            cad = procurar(cpf, listas[command2])
            if cad:

                #Apresentar Cadastro
                if command == 2:
                    cad.apresentar_cad()

                #Modificar Cadastro
                elif command == 3:
                    cad.modificar_cad()
                    print('CADASTRO MODIFICADO')

                #Remover Cadastro
                elif command == 4:
                    cad.remover_cad(listas[command2])
                    print('CADASTRO REMOVIDO')

        #Saída
        saida = input('Voltar ao MENU(s/n):')







