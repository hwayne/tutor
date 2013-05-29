import unittest
import lexer

class Tests(unittest.TestCase):
   
    def setUp(self):
        self.L = lexer.Lexer()

    def testBase(self):
        self.assertFalse(False)

    def testLexOne(self):
        self.assertEqual(self.L.lexString("+"), ["PLUS"])

    def testLexTwo(self):
        self.assertEqual(self.L.lexString("+-"), ["PLUS", "MINUS"])

    def testLexGreedy(self):
        self.assertEqual(self.L.lexString("++-"), ["PLUSPLUS", "MINUS"])

    def testLexDigit(self):
        self.assertEqual(self.L.lexString("113"), ["113"])

    def testLexEqn(self):
        self.assertEqual(self.L.lexString("23+45"), ["23", "PLUS", "45"])


if __name__ == "__main__":
   unittest.main()
