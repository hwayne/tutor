tokendict = {
"+"    : "PLUS"
,"++"  : "PLUSPLUS" #testing purposes
,"-"   : "MINUS"
,"*"   : "TIMES"
,"/"   : "DIVIDE"
,"("   : "LPAREN"
,")"   : "RPAREN"
,"^"   : "EXPONENT"
,"%"   : "MOD"
        }

parsedict = dict([token[::-1] for token in tokendict.iteritems()]) #So we can recombine
parsedict["NEG"]="-" #For negatives
parsedict["EXPONENT"] = "**"

#For operator errors
ops = [tokendict["+"], tokendict["-"], tokendict["*"]]

#For tree validation
nodeops = ops+[tokendict["/"], tokendict["%"]]

#For operator priority
priority = {"PLUS": 1, "MINUS": 1, "MOD": 1,
            "TIMES": 2, "DIVIDE": 2} #NEG?
            #"LPAR": 3?
