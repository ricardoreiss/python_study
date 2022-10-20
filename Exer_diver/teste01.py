class Veterinario():
    def __init__(self,):
        self.nome = input("\nNome: ")
        self.idade = int(input("Idade: "))
        self.raça = input("Raça: ")

    def apresentaCadastro(self):
        print("\n------Cadastro------")
        print("Nome: ", self.nome)
        print("Idade: ", self.idade)
        print("Raça: ", self.raça)
        print("--------------------\n")

class Entrada():
    def apresentaMenu():
        print("1 - Cadastrar novo animal")
        print("2 - Apresentar todos os cadastros de animais")
        print("3 - Consultar cadastro por raça")
        opc = int(input("Digite sua opção: "))

        return opc

    listaDeAnimal = list()
    cont = 0
    qtdAnimal = 0
    while True:

        opc = apresentaMenu()
        print(opc)

        if (opc == 1):
            qtdAnimal += 1
            animal = Veterinario()

            listaDeAnimal.append(animal)

        elif (opc == 2):
            print(listaDeAnimal)
            for ani in listaDeAnimal:
                ani.apresentaCadastro()

        elif (opc == 3):
            raça = input("Digite a raça a ser consultada: ")
            achou = False
            for ani in listaDeAnimal:
                if (raça == ani.raça):
                    ani.apresentaCadastro()
                    achou = True

            if achou == False:
                print("Cadastro não encontrado")

            if (opc < 1 or opc > 3):
                print("Digite uma opção valida")

