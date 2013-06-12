import unittest
from errors import errors
import tokens

class TestError(unittest.TestCase):
   
    def setUp(self):
        pass

    def testIdentity(self):
        self.assertEquals(errors.identity(["6","PLUS","7"]), ["6","PLUS", "7"])

#The list comprehension is because each error also returns what kind of error it is, information we don't need for the tests.

    def testOpWalk(self):
        variants = errors.operror(["6","PLUS","7"])
        self.assertIn(["6","TIMES","7"], [x[0] for x in variants])

    def testOpWalkTwo(self):
        variants = errors.operror(["8","PLUS","2"])
        self.assertIn(["8","MINUS","2"], [x[0] for x in variants])

    def testMultiOpWalk(self):
        variants = errors.operror(["8","PLUS","2", "MINUS", "3"])
        self.assertIn(["8","MINUS","2", "MINUS", "3"], [x[0] for x in variants])
        self.assertIn(["8","PLUS","2", "TIMES", "3"], [x[0] for x in variants])
        self.assertNotIn(["8","TIMES","2", "TIMES", "3"], [x[0] for x in variants]) #Not recursive... yet

    def testCut(self):
        self.assertEquals(errors.cut(["MINUS", "4", "MINUS"], 1, 1, tokens.ops), 2)

    def testNestedCut(self):
        self.assertEquals(errors.nestedcut(["LPAREN", "LPAREN", "RPAREN", "RPAREN"], 0, 1, ["RPAREN"], "LPAREN", "RPAREN"), 3)

#Associative errors

    def testAssocWalk(self):
        variants = errors.assocerror(["8", "MINUS", "4", "MINUS", "2"])
        self.assertIn(["8", "MINUS", "LPAREN", "4", "MINUS", "2", "RPAREN"], [x[0] for x in variants])

    def testAssocWalk(self):
        variants = errors.assocerror(["8", "MINUS", "4", "MINUS", "2"])
        self.assertIn(["8", "MINUS", "LPAREN", "4", "MINUS", "2", "RPAREN"], [x[0] for x in variants])

    def testMultiAssocWalk(self):
        variants = errors.assocerror(["8", "MINUS", "4", "MINUS", "2", "MINUS", "1"])
        self.assertIn(["8", "MINUS", "LPAREN", "4", "MINUS", "2", "RPAREN", "MINUS", "1"], [x[0] for x in variants])

#Dropped negatives

    def testNegWalk(self):
        
        variants = errors.negerror(["NEG", "1", "PLUS", "NEG", '2'])
        self.assertIn(["1", "PLUS", '2'], [x[0] for x in variants])
        self.assertIn(["NEG", "1", "PLUS", '2'], [x[0] for x in variants])

    #Parenthesis removal tests

    def testDeParen(self):
        variants = errors.parenerror(["1", "PLUS", "LPAREN", "2", "TIMES", "3", "RPAREN"])
        self.assertIn(["1", "PLUS", '2', 'TIMES', '3'], [x[0] for x in variants])
#Test get all errors

    def testErrorSet(self):
        variants = errors.geterrorset(["NEG", "1", "PLUS", "2"], errors.alloperatorerrors)
        self.assertIn(["1", "PLUS", '2'], [x[0] for x in variants])
        self.assertIn(["NEG", "1", "TIMES", '2'], [x[0] for x in variants])

#END tests
if __name__ == "__main__":
   unittest.main()
