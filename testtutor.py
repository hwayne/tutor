import unittest
import tutor

class TestLexer(unittest.TestCase):
   
    def setUp(self):
        self.T = tutor.Tutor()

    def testSolve(self):
        self.assertEquals(self.T.solve(["6","PLUS","7"]), 13)

    def testSolveTwo(self):
        self.assertEquals(self.T.solve(["6","PLUS","9"]), 15)

    def testFullStack(self):
        self.assertEquals(self.T.solve(
            self.T.lexer.lexString("13+23")), 36)

    def testOpError(self):
        self.T.setup("3+4")
        self.assertIn(12, self.T.errorlist.keys())

    def testOpErrorTwo(self):
        self.T.setup("3+5")
        self.assertIn(-2, self.T.errorlist.keys())

    def testCheck(self):
        self.T.setup("7+8")
        self.assertTrue(self.T.check(15))

    def testFalseCheck(self):
        self.T.setup("6+10")
        self.assertFalse(self.T.check(15))

if __name__ == "__main__":
   unittest.main()
