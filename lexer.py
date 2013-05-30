import itertools
from tokens import tokendict 

class Lexer():

    def __init__(self):
        self.tokendict = tokendict
        pass

#Replaces appropriate MINUSes with NEGs.
    def clean(self, s):
        temp = s[:]
        for i, token in enumerate(s):
            if(token == "MINUS") and (i == 0 or not(s[-i].isdigit() or s[-i] == "RPAREN")): #Holy SHIT.
                temp[i] = "NEG"
        return temp

    def lexString(self, s):
       tokens = []
       temp = ""
       tokenlist = self.tokendict.keys()
       for elem in s+"@": #Temporary, while I fix token loop
           if (temp).isdigit() and not (temp+elem).isdigit():
               tokens.append(temp)
               temp = ""
           #elif temp=="" and elem not in self.tokendict.keys():
           #    return "MAYDAY" #invalid token
           elif temp in tokenlist and (temp+elem) not in tokenlist: #get longest matching token
               tokens.append(self.tokendict[temp])
               temp = ""
           temp += elem
       #tokens.append(self.tokendict[temp[0]]) #edge case
       return self.clean(tokens)

if __name__ == "__main__":
    
    L = Lexer()

    while True:
        print L.lexString(raw_input())
