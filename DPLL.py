import sys

#We will define variables in lowercase as variables with no negation and characters in uppercase as variables in negation
# -a = A
# a = a

#Definitions--------------------------------------------------------

#CLI Arguments
args = sys.argv[1:]

#Later will be the list of variables
vars = []

#Help-Methods------------

#checks whether a character c exists in character list varlist
#return True: c doesn't exist in varlist
#return False: c does exist in varlist
def setCheck(c, varList):
    for c_ in varList:
        if(c==c_):
            return False
    return True

#Get the index of an element of a list
def getIndex(list, el):
    for i in range(len(list)):
        if(el == list[i]):
            return i
    return -1

def setVarTrue(clause, char):
    #Generation of trueBranch
    returnValue = []
    for lit in clause:
        if(not setCheck(char.lower(), lit)):
            continue
        temp = lit.replace(char.upper(), "")
        if(setCheck(temp, returnValue)):
            returnValue.append(temp)
    return returnValue

def setVarFalse(clause, char):
    #Generation of falseBranch
    returnValue = []
    for lit in clause:
        if(not setCheck(char.upper(), lit)):
            continue
        temp = lit.replace(char.lower(), "")
        if(setCheck(temp, returnValue)):
            returnValue.append(temp)
    return returnValue


#End Help-Methods--------

#Base DPLL
#clause: a list of strings
#vars: list of variables (just so that no global vars are used)
#depth: Recursion(assuming no heuristics) depth and index of the current character
#inter: Interpretation - Belegung in german
def base_DPLL(clause, vars, depth, inter):
    #Checks whether to end Recursion
    if(len(clause)==0):
        print("Done, A valid interpretation:")
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
    trueBranch = setVarTrue(clause, char)

    #Print Debug
    #print(trueBranch)
    inter[depth] = 1
    print(str(trueBranch) + ": " + vars[depth] + " = 1")
    if(DPLL_Step(trueBranch, vars, depth+1, inter)):
        return True

    #Generation of falseBranch
    falseBranch = setVarFalse(clause, char)

    #Print Debug
    #print(falseBranch)

    inter[depth] = 0
    print(str(falseBranch) + ": " + vars[depth] + " = 0")
    if(DPLL_Step(falseBranch, vars, depth+1, inter)):
        return True

    return False

#Heuristics

#One Literal Rule
def OLR(clause, vars, depth, inter):
    bool = False
    char = None
    for i in range(len(clause)):
        if(len(clause[i]) == 1):
            bool = True
            char = clause[i][0]
            break

    if(bool):
        temp = []
        if(char.isupper()):
            temp = setVarFalse(clause, char)
            inter[getIndex(vars, char.lower())] = 0
        else:
            temp = setVarTrue(clause, char)
            inter[getIndex(vars, char.lower())] = 1
        print(str(temp) + " OLR")
        return DPLL_Step(temp, vars, depth, inter)
    else:
        return PLR(clause, vars, depth, inter)


#Pure Literal Rule
def PLR(clause, vars, depth, inter):
    bool = False
    char = None
    temp = []
    for cl in clause:
        for c in cl:
            if(setCheck(c, temp)):
                temp.append(c)
    temp = [c.lower() for c in temp]
    temp.sort()
    i = 0
    while(i<len(temp)):
        i_ = 1
        while((i_+i) < len(temp) and temp[i+i_] == temp[i]):
            i_ = i_+1
        if(i_ == 1):
            bool = True
            char = temp[i]
            break
        i = i+i_

    if(bool):
        temp = []
        if(char.isupper()):
            temp = setVarFalse(clause, char)
            inter[getIndex(vars, char.lower())] = 0
        else:
            temp = setVarTrue(clause, char)
            inter[getIndex(vars, char.lower())] = 1
        print(str(temp) + " PLR")
        return DPLL_Step(temp, vars, depth, inter)
    else:
        return base_DPLL(clause, vars, depth, inter)

#Because there are heuristics to consider, we will define the OLR->PLR->Base_DPLL sequencec as a step.
def DPLL_Step(clause, vars, depth, inter):
    return OLR(clause, vars, depth, inter)


#Initializing function
def DPLL(clause, vars):
    inter = []
    for v in vars:
        inter.append(-1) #-1 if an interpretation isnt assigned
    if not DPLL_Step(clause, vars, 0, inter):
        print("Not solveable :(")
    return


#Code---------------------------------------------------------------

#Generation of variable list
for arg in args:
    temp = arg.lower()
    for c in temp:
        if(setCheck(c, vars)):
            vars.append(c)
vars.sort()

print(str(args) + " Starting DPLL...")
DPLL(args, vars)
