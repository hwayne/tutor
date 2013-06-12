import unittest
from lexers import eqntree

class TestEqntree(unittest.TestCase):

    def testTrue(self):
        self.assertTrue(True)

    def testFlattenSimpleTree(self):
        tree = ("PLUS", ["2"],("TIMES", ["2"], ["2"]))
        flattree = ["2", "PLUS", "2", "TIMES", "2"]
        self.assertEquals(eqntree.flattenTree(tree), flattree)

    def testIsTree(self):
        tree =  ("PLUS", ["2"],("TIMES", ["2"], ["2"])) 
        self.assertTrue(eqntree.isTree(tree))

    def testIsNotTree(self):
        tree =  (["2"],("TIMES", ["2"], ["2"])) 
        self.assertFalse(eqntree.isTree(tree))

    def testIsAlsoNotTree(self):
        tree =  ("NEG",["2"],("TIMES", ["2"], ["2"])) 
        self.assertFalse(eqntree.isTree(tree))

if __name__ == "__main__":
    unittest.main()
