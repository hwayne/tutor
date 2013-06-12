import unittest
from lexers import lexer
from tokens import parsedict

class TestLexer(unittest.TestCase):
   
    def setUp(self):
        self.L = lexer.Lexer()

    def testBase(self):
        self.assertFalse(False)

    def testLexOne(self):
        self.assertEqual(self.L.lexString("+"), ["PLUS"])

    def testLexTwo(self):
        self.assertEqual(self.L.lexString("+*"), ["PLUS", "TIMES"])

    def testLexGreedy(self):
        self.assertEqual(self.L.lexString("++*"), ["PLUSPLUS", "TIMES"])

    def testLexDigit(self):
        self.assertEqual(self.L.lexString("113"), ["113"])

    def testLexEqn(self):
        self.assertEqual(self.L.lexString("23+45"), ["23", "PLUS", "45"])

    def testClean(self):
        self.assertEqual(self.L.lexString("-1"), ["NEG", "1"])
    
    def testNotClean(self):
        self.assertEqual(self.L.lexString("6*1-1"),['6', 'TIMES', '1', 'MINUS', '1'])

#END tests
class TestParser(unittest.TestCase):
  
    #def setUp(self):
        #self.P = parser.Parser()
     def testParser(self):
         self.assertIn("PLUS", parsedict)

if __name__ == "__main__":
   unittest.main()
