from lexer import Lexer
import tokens
import errors

class Tutor():

    def __init__(self):
        self.lexer = Lexer()
        self.string = ""
        self.tokenstring = []
        self.solution = 0
        self.errorlist = {}

    def parse(self, problemtokens):
        problem = ""
        for elem in problemtokens:
            if elem.isdigit():
                problem += elem
            else:
                problem += tokens.parsedict[elem]
        return problem

    def solve(self, problemtokens):
        solution = eval(self.parse(problemtokens)) #I love eval
        return solution

#This function is a slight misnomer. It finds both the actual solution (no longer!) and builds the error tree.
#It does it by calling the appropriate error functions on our token string. Then if the new problems give us a unique answer, stick it in. 
#Possible improvement: error dictionary, so you can select the errors.

    def buildErrorTree(self):
        operrors = errors.operror(self.tokenstring)
        assocerrors = errors.assocerror(self.tokenstring)
        for elem in operrors+assocerrors:
            wronganswer = self.solve(elem[0])
            if wronganswer != self.solution and wronganswer not in self.errorlist.keys():
                self.errorlist[wronganswer] = elem

    def setup(self, string):
        self.string = string
        self.tokenstring = self.lexer.lexString(string) 
        self.solution = self.solve(self.tokenstring)
        self.buildErrorTree()

    def check(self, guess):
        return self.solution == int(guess)

#Untested because it's a print string. Tested manually.
    def giveAnswer(self, guess):
        if self.check(guess):
            print "Correct!"
        else:
            print "Incorrect"
            if guess in self.errorlist.keys(): 
                mistake = self.errorlist[guess]
                print "Most likely mistake: " + mistake[1]
                print "Equivalent problem: " + self.parse(mistake[0])
            else:
                print "No determined likely mistake."

if __name__ == "__main__":
    T = Tutor()
    #T.setup(raw_input("Enter arithmatic problem: "))
    print "Problem: 5+3"
    T.setup("5+3")
    guess = int(raw_input("Enter solution: "))
    
    T.giveAnswer(guess)
