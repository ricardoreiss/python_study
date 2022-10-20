

class Node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None


class Tree:
    def __init__(self):
        self.root=None

    def insert(self,value):
        self._insert(value,self.root)

    def _insert(self,value,atual=None):
      
        if self.root==None:
            self.root=Node(value)
            atual=self.root
            atual.value=value
        else:

            if atual!=None:
                if value>=atual.value:
                    if atual.right==None:
                        atual.right=Node(value)
                    else:
                        self._insert(value,atual.right)
                else:
                    if atual.left==None:
                        atual.left=Node(value)
                    else:
                        self._insert(value,atual.left)

    def print(self):
        self._print(self.root)

    retorno = []
    def _print(self,atual=None):

        if atual!=None:
            print(str(atual.value)+",")
            self.retorno.append(atual.value)
            self._print(atual.left)
            self._print(atual.right)

        return self.retorno

"""tree=Tree()
command=""
while command!="s":

    command=input("inserir(i),print(p):")

    if command=="i":
        value=float(input("digite um número:"))
        tree.insert(value)
    else:
        if command=="p":
            tree.print()

print("saiu")"""




