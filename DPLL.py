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



def setVarTrue(clause, char):
    #Generation of trueBranch
    returnValue = []
    for lit in clause:
        if(not setCheck(char, lit)):
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
        temp = lit.replace(char, "")
        if(setCheck(temp, returnValue)):
            returnValue.append(temp)


#End Help-Methods--------

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
    trueBranch = setVarTrue(clause, char)

    #Print Debug
    #print(trueBranch)
    inter[depth] = 1
    if(DPLL_Step(trueBranch, vars, depth+1, inter)):
        return True

    #Generation of falseBranch
    falseBranch = setVarFalse(clause, char)

    #Print Debug
    #print(falseBranch)

    inter[depth] = 0
    if(DPLL_Step(falseBranch, vars, depth+1, inter)):
        return True

    return False

#Heuristics

#One Literal Rule
def OLR(clause, vars, depth, inter):
    bool = False
    char = None
    for lit in clause:
        if(len(lit) == 1):
            bool = True
            char = lit[0]
            break

    if(bool):
        temp = []
        if(char.isupper()):
            temp = setVarFalse(clause, char)
        else:
            temp = setVarTrue(clause, char)
        print(temp)
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
    temp.sort()
    for i in range(len(temp)):
        i_ = 1
        while((i_+i) < len(temp) and temp[i+i_].lower() == temp[i].lower()):
            i_ = i_+1
        if(i_ == 1):
            bool = True
            char = temp[i]
            break

    if(bool):
        temp = []
        if(char.isupper()):
            temp = setVarFalse(clause, char)
        else:
            temp = setVarTrue(clause, char)
        print(temp)
        return DPLL_Step(temp, vars, depth, inter)
    else:
        return base_DPLL(clause, vars, depth, inter)

#Because there are heuristics to consider, we will define the OLR->PLR->Base_DPLL sequencec as a step.
def DPLL_Step(clause, vars, depth, inter):
    OLR(clause, vars, depth, inter)


#Initializing function
def DPLL(clause, vars):
    inter = []
    for v in vars:
        inter.append(-1) #-1 if an interpretation isnt assigned
    DPLL_Step(clause, vars, 0, inter)
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
