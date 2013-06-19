import unittest
from lexers import tokentree 

class TestEqntree(unittest.TestCase):

    def testTrue(self):
        self.assertTrue(True)

    def testFlattenSimpleTree(self):
        tree = ("PLUS", ["2"],("TIMES", ["2"], ["2"]))
        flattree = ["2", "PLUS", "2", "TIMES", "2"]
        self.assertEquals(tokentree.flatten_tree(tree), flattree)

    def testIsTree(self):
        tree =  ("PLUS", ["2"],("TIMES", ["2"], ["2"])) 
        self.assertTrue(tokentree.is_tree(tree))

    def testIsNotTree(self):
        tree =  (["2"],("TIMES", ["2"], ["2"])) 
        self.assertFalse(tokentree.is_tree(tree))

    def testIsAlsoNotTree(self):
        tree =  ("NEG",["2"],("TIMES", ["2"], ["2"])) 
        self.assertFalse(tokentree.is_tree(tree))

    def testBuildTree(self):
        tree = tokentree.TokenTree(["1", "PLUS", "2"])
        self.assertEquals(tree.tokentree, ("PLUS", ['1'], ['2']))

    def testBuildNestedTree(self):
        tokenstring = ["1", "PLUS", "2", "PLUS", "3"]
        tree = tokentree.TokenTree(tokenstring)
        self.assertEquals(tree.tokentree, ("PLUS", ("PLUS", ['1'], ['2']), ['3']))

    def testBuildNegaTree(self):
        tokenstring = ["1", "MINUS", "2", "MINUS", "3"]
        tree = tokentree.TokenTree(tokenstring)
        self.assertEquals(tree.tokentree, ("MINUS", ("MINUS", ['1'], ['2']), ['3']))

    def testBuildPriorityTree(self):
        tokenstring = ["2", "PLUS", "2", "TIMES", "2"]
        tree = tokentree.TokenTree(tokenstring)
        self.assertEquals(tree.tokentree, ("PLUS", ['2'], ('TIMES', ['2'], ['2'])))

    def testParen(self):
        tokenstring = ['2', 'TIMES', 'LPAREN', '2', 'PLUS', '2', 'RPAREN']
        tree = tokentree.TokenTree(tokenstring)
        target = ('TIMES', ['2'], ('PLUS', ['LPAREN', '2'], ['2', 'RPAREN']))
        self.assertEquals(tree.tokentree, target)

    def testOtherParen(self):
        tokenstring = ['LPAREN', '2', 'PLUS', '2', 'RPAREN', 'TIMES', '2']
        tree = tokentree.TokenTree(tokenstring)
        target = ('TIMES', ('PLUS', ['LPAREN', '2'], ['2', 'RPAREN']), ['2'])
        self.assertEquals(tree.tokentree, target)

    def testBreakParenCase(self):
        tokenstring = ['LPAREN', '2', 'PLUS', '2', 'RPAREN', 'MINUS', 'LPAREN', '2', 'PLUS', '2', 'RPAREN']
        tree = tokentree.TokenTree(tokenstring)
        target = ('MINUS', ('PLUS', ['LPAREN', '2'], ['2', 'RPAREN']), ('PLUS', ['LPAREN', '2'], ['2', 'RPAREN']))
        self.assertEquals(tree.tokentree, target)

    def testBuildNegs(self):
        tokenstring = ['2', 'PLUS', 'NEG', '1']
        target = ('PLUS', ['2'], ['NEG', '1'])
        tree = tokentree.TokenTree(tokenstring)
        self.assertEquals(tree.tokentree, target)

    def testParenNegs(self):
        tokenstring = ['2', 'PLUS', 'LPAREN', 'NEG', '1', 'RPAREN']
        target = ('PLUS', ['2'], ['LPAREN', 'NEG', '1', 'RPAREN'])
        tree = tokentree.TokenTree(tokenstring)
        self.assertEquals(tree.tokentree, target)


if __name__ == "__main__":
    unittest.main()
