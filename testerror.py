import unittest
import errors

class TestLexer(unittest.TestCase):
   
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

if __name__ == "__main__":
   unittest.main()
