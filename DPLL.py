#!/usr/bin/python3

import sys
from enum import Enum, auto
#We will define variables in lowercase as variables with no negation and characters in uppercase as variables in negation
# -a = A
# a = a

#Definitions--------------------------------------------------------

#Enum to cover the case:
#FALSE: The DPLL recursion should go on with false
#TRUE: The DPLL recursion should go on with true
#BOTH: The DPLL recursion should go on with both branches
class RecType(Enum):
	FALSE = auto()
	TRUE = auto()
	BOTH = auto()

#Defining type of recursion.
#var: defines which variable will be used next
#type: defines which branches the recursion will take
class NextRec:
	def __init__(self, var, recType):
		self.var = var
		self.type = recType

#checks whether a character c exists in character list varlist
#return True: c doesn't exist in varlist
#return False: c does exist in varlist
def setCheck(c, varList):
    for c_ in varList:
        if(c==c_):
            return False
    return True

#Gets the next variable to use. If no heuristic it just uses the order of
# variables in vars to determine which variable is next.
#If a heuristic is applicable, that heuristic is used.
def getNextRec(clause, vars):
	#TODO code for OLR/PLR heuristic

	c = '?'

	clauseVars = ""

	for lit in clause:
		clauseVars += lit

	clauseVars = clauseVars.lower()

	for i in range(len(vars)):
		if(not setCheck(vars[i], clauseVars)):
			c = vars[i]
			break

	#print("Char: " + c)

	return NextRec(c, RecType.BOTH)

def genBranch(clause, nextRec, bool):
	branch = []
	
	if(bool):
		#Generation of trueBranch
	    for lit in clause:
	        if(not setCheck(nextRec.var, lit)):
	            continue
	        temp = lit.replace(nextRec.var.upper(), "")
	        if(setCheck(temp, branch)):
	            branch.append(temp)
	else:
		#Generation of falseBranch
	    for lit in clause:
	        if(not setCheck(nextRec.var.upper(), lit)):
	            continue
	        temp = lit.replace(nextRec.var, "")
	        if(setCheck(temp, branch)):
	            branch.append(temp)

	return branch

#Sets the interpretation of var with the value of bool. The value of bool is True, False
#but inter is an array of 0 and 1
def setInter(inter, vars, var, bool):
	for i in range(len(vars)):
		if(vars[i] == var):
			inter[i] = 1 if bool else 0

#Base DPLL
#clause: a list of strings
#vars: list of variables (just so that no global vars are used)
#inter: Interpretation - Belegung in german
def base_DPLL(clause, vars, inter):

    #Checks whether to end Recursion
    if(len(clause)==0):
        print(vars)
        print(inter)
        return True
    else:
        for lit in clause:
            if(lit == ""):
                return False

    #print(vars)
    #print(clause)

    nextRec = getNextRec(clause, vars)

    if(nextRec.type == RecType.TRUE or nextRec.type == RecType.BOTH):
    	#Generation of trueBranch
    	trueBranch = genBranch(clause, nextRec, True)
    	setInter(inter, vars, nextRec.var, True)
    	
    	if(base_DPLL(trueBranch, vars, inter)):
        	return True

    if(nextRec.type == RecType.FALSE or nextRec.type == RecType.BOTH):
	    #Generation of falseBranch
	    falseBranch = genBranch(clause, nextRec, False)
	    setInter(inter, vars, nextRec.var, False)
	    
	    if(base_DPLL(falseBranch, vars, inter)):
        	return True


    return False

#Initializing function
def DPLL(clause, vars):
    inter = []
    for v in vars:
        inter.append(-1) #-1 if an interpretation isnt assigned
    base_DPLL(clause, vars, inter)
    return


#Global Variables---------------------------------------------------

#CLI Arguments
g_args = sys.argv[1:]

#Later will be the list of variables
g_vars = []

#Code---------------------------------------------------------------

#Generation of variable list
for arg in g_args:
    temp = arg.lower()
    for c in temp:
        if(setCheck(c, g_vars)):
            g_vars.append(c)
g_vars.sort()

DPLL(g_args, g_vars)
