import unittest
import bintree


"""class TestBinTreeMethods():

    def test_calcAltura(self):
        tree = bintree.Tree()
        tree.insert(4)
        tree.insert(6)
        tree.insert(5)
        tree.insert(7)
        tree.insert(2)
        tree.insert(1)
        tree.insert(3)
        #self.assertEqual(tree.calcAltura(), 3)"""

def test_inserir():
    self.tree = bintree.Tree()
    self.tree.insert(4)
    self.tree.insert(6)
    self.tree.insert(5)
    self.tree.insert(7)
    self.tree.insert(2)
    self.tree.insert(1)
    self.tree.insert(3)
    print(self.tree._print())
    #self.assertEqual(tree._print(), [4, 2, 1, 3, 6, 5, 7])

test_inserir()
"""if __name__ == '__main__':
    unittest.main()"""

