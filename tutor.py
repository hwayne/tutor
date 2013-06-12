from lexers.lexer import Lexer
import tokens
from errors import errors

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

    #Removes errors that give duplicate and/or correct solutions fromthe dictionary.

    def addUniqueErrors(self, errorlist):
        uniques = []
        for elem in errorlist:
            wronganswer = self.solve(elem[0])
            if wronganswer != self.solution and wronganswer not in self.errorlist.keys():
                self.errorlist[wronganswer] = elem
                uniques.append(elem)
        return uniques #For recursive build
#Builds a new error tree by calling the appropriate error functions on our token string. 
#Then if the new problems give us a unique answer, stick it in. 
#Possible improvement: error dictionary, so you can select the errors.

    def buildErrorSpace(self):
        allerrors = errors.geterrorset(self.tokenstring, errors.alloperatorerrors)
        self.addUniqueErrors(allerrors)

#Quick and dirty. Take list of tuples, return first elements.
#Helps us grab token strings in solve list
#Not actually used. How 'bout that.

    def firstElements(self,tuplelist):
        return [x[0] for x in tuplelist]

#Recursively builds the entire error space. Does this by applying all error transformations to each error.
#Then determines which of these lead to unique solutions, and then use the results for the next round.
#Ends when no new useful errors are found.
#The entire error check system needs to be seriously reworked.

    def buildRecursiveErrorSpace(self):
        newerrors =   errors.geterrorset(self.tokenstring, errors.alloperatorerrors)
        newerrors = self.addUniqueErrors(newerrors) #Gettem out of the way, + reduce search space 
      
        while newerrors != []:
            for elem in newerrors[:]:
                nexterrors =  errors.geterrorset(elem[0], errors.alloperatorerrors)

                nexterrors = self.addUniqueErrors([(x[0], elem[1]+", "+x[1]) for x in nexterrors])
                newerrors += nexterrors
                newerrors.remove(elem)
        
    def setup(self, string, recursive = False):
        self.string = string
        self.tokenstring = self.lexer.lexString(string) 
        self.solution = self.solve(self.tokenstring)
        if recursive:
            self.buildRecursiveErrorSpace()
        else:
            self.buildErrorSpace()

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
                 
                print "Most likely mistake"+("s"*(',' in mistake[1]))+": " + mistake[1]
                print "Equivalent problem: " + self.parse(mistake[0])
            else:
                print "No determined likely mistake."

if __name__ == "__main__":
    T = Tutor()
    
    T.setup(raw_input("Enter arithmatic problem: "), True)
    guess = int(raw_input("Enter solution: "))
    
    T.giveAnswer(guess)
