import sys

#We will define variables in lowercase as variables with no negation and characters in uppercase as variables in negation
# -a = A
# a = a

#Definitions--------------------------------------------------------

#CLI Arguments
args = sys.argv[1:]

#Later will be the list of variables
vars = []

#checks whether a character c exists in character list varlist
#return True: c doesn't exist in varlist
#return False: c does exist in varlist
def setCheck(c, varList):
    for c_ in varList:
        if(c==c_):
            return False
    return True

#Base DPLL
#clause: a list of strings
#vars: list of variables (just so that no global vars are used)
#depth: Recursion(assuming no heuristics) depth and index of the current character
#inter: Interpretation - Belegung in german
def base_DPLL(clause, vars, depth, inter):
    #Checks whether to end Recursion
    if(len(clause)==0):
        print(vars)
        print(inter)
        return True
    else:
        for lit in clause:
            if(lit == ""):
                return False

    trueBranch = []
    falseBranch = []
    char = vars[depth]

    #Generation of trueBranch
    for lit in clause:
        if(not setCheck(char, lit)):
            continue
        temp = lit.replace(char.upper(), "")
        if(setCheck(temp, trueBranch)):
            trueBranch.append(temp)

    #Print Debug
    #print(trueBranch)
    inter[depth] = 1
    if(base_DPLL(trueBranch, vars, depth+1, inter)):
        return True

    #Generation of trueBranch
    for lit in clause:
        if(not setCheck(char.upper(), lit)):
            continue
        temp = lit.replace(char, "")
        if(setCheck(temp, falseBranch)):
            falseBranch.append(temp)

    #Print Debug
    #print(falseBranch)

    inter[depth] = 0
    if(base_DPLL(falseBranch, vars, depth+1, inter)):
        return True

    return False

def OLR():
    pass

def PLR():
    pass

#Initializing function
def DPLL(clause, vars):
    inter = []
    for v in vars:
        inter.append(-1) #-1 if an interpretation isnt assigned
    base_DPLL(clause, vars, 0, inter)
    return


#Code---------------------------------------------------------------

#Generation of variable list
for arg in args:
    temp = arg.lower()
    for c in temp:
        if(setCheck(c, vars)):
            vars.append(c)
vars.sort()
DPLL(args, vars)
