import unittest
from errors import errortools
import tokens

class TestErrorTools(unittest.TestCase):

    def testCut(self):
        self.assertEquals(errortools.cut(["MINUS", "4", "MINUS"], 1, tokens.ops), 2)

    def testNestedCut(self):
        self.assertEquals(errortools.cut(["LPAREN", "LPAREN", "RPAREN", "RPAREN"], 0, ["RPAREN"], 1, "LPAREN", "RPAREN"), 3)

#END tests
if __name__ == "__main__":
   unittest.main()
