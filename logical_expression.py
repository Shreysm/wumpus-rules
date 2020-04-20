#Author:Shreyas Mohan
#StudentId:1001669806
#!/usr/bin/env python

#-------------------------------------------------------------------------------
# Name:        logical_expression
# Purpose:     Contains logical_expression class, inference engine,
#              and assorted functions
#
# Created:     09/25/2011
# Last Edited: 07/22/2013  
# Notes:       *This contains code ported by Christopher Conly from C++ code
#               provided by Dr. Vassilis Athitsos
#              *Several integer and string variables are put into lists. This is
#               to make them mutable so each recursive call to a function can
#               alter the same variable instead of a copy. Python won't let us
#               pass the address of the variables, so put it in a list which is
#               passed by reference. We can also now pass just one variable in
#               the class and the function will modify the class instead of a
#               copy of that variable. So, be sure to pass the entire list to a
#               function (i.e. if we have an instance of logical_expression
#               called le, we'd call foo(le.symbol,...). If foo needs to modify
#               le.symbol, it will need to index it (i.e. le.symbol[0]) so that
#               the change will persist.
#              *Written to be Python 2.4 compliant for omega.uta.edu
#-------------------------------------------------------------------------------

import sys
from copy import copy
import copy
#-------------------------------------------------------------------------------
# Begin code that is ported from code provided by Dr. Athitsos
class logical_expression:
    """A logical statement/sentence/expression class"""
    # All types need to be mutable, so we don't have to pass in the whole class.
    # We can just pass, for example, the symbol variable to a function, and the
    # function's changes will actually alter the class variable. Thus, lists.
    def __init__(self):
        self.symbol = ['']
        self.connective = ['']
        self.subexpressions = []

def getsym(symbols, kb=[],st=[]):
    if not kb==[]:
        if kb.symbol[0]:
            symbols.append(kb.symbol[0])
        for i in kb.subexpressions:
            getsym(symbols,i)
    if not st==[]:
        if st.symbol[0]:
            symbols.append(st.symbol[0])
        for i in st.subexpressions:
            getsym(symbols,i)


def print_expression(expression, separator):
    """Prints the given expression using the given separator"""
    if expression == 0 or expression == None or expression == '':
        print '\nINVALID\n'

    elif expression.symbol[0]: # If it is a base case (symbol)
        sys.stdout.write('%s' % expression.symbol[0])

    else: # Otherwise it is a subexpression
        sys.stdout.write('(%s' % expression.connective[0])
        for subexpression in expression.subexpressions:
            sys.stdout.write(' ')
            print_expression(subexpression, '')
            sys.stdout.write('%s' % separator)
        sys.stdout.write(')')


def read_expression(input_string, counter=[0]):
    """Reads the next logical expression in input_string"""
    # Note: counter is a list because it needs to be a mutable object so the
    # recursive calls can change it, since we can't pass the address in Python.
    result = logical_expression()
    length = len(input_string)
    while True:
        if counter[0] >= length:
            break

        if input_string[counter[0]] == ' ':    # Skip whitespace
            counter[0] += 1
            continue

        elif input_string[counter[0]] == '(':  # It's the beginning of a connective
            counter[0] += 1
            read_word(input_string, counter, result.connective)
           # print(result.connective)
           # print("DONE")
            read_subexpressions(input_string, counter, result.subexpressions)
           # print("Here")
           # print(result.subexpressions)
            #h=input("fe")
            break

        else:  # It is a word
            read_word(input_string, counter, result.symbol)
            break

    return result


def read_subexpressions(input_string, counter, subexpressions):
    """Reads a subexpression from input_string"""
   # print("Entered exps")
    length = len(input_string)
    while True:
        if counter[0] >= length:
            print '\nUnexpected end of input.\n'
            return 0

        if input_string[counter[0]] == ' ':     # Skip whitespace
            counter[0] += 1
            continue

        if input_string[counter[0]] == ')':     # We are done
            counter[0] += 1
            return 1

        else:
            expression = read_expression(input_string, counter)
            #print(expression)
            #h=input("Got ot")
            subexpressions.append(expression)
    #print("Leaving exps")


def read_word(input_string, counter, target):
    """Reads the next word of an input string and stores it in target"""
    #print("entered readword")
    word = ''
    while True:
        if counter[0] >= len(input_string):
            break

        if input_string[counter[0]].isalnum() or input_string[counter[0]] == '_':
            target[0] += input_string[counter[0]]
            counter[0] += 1
     #       print(target[0])
           # g=input("ReadWord just got printed")

        elif input_string[counter[0]] == ')' or input_string[counter[0]] == ' ':
            break

        else:
            print('Unexpected character %s.' % input_string[counter[0]])
            sys.exit(1)
    #print("Leaving readword")


def valid_expression(expression):
    """Determines if the given expression is valid according to our rules"""
    if expression.symbol[0]:
        return valid_symbol(expression.symbol[0])

    if expression.connective[0].lower() == 'if' or expression.connective[0].lower() == 'iff':
        if len(expression.subexpressions) != 2:
            print('Error: connective "%s" with %d arguments.' %
                        (expression.connective[0], len(expression.subexpressions)))
            return 0

    elif expression.connective[0].lower() == 'not':
        if len(expression.subexpressions) != 1:
            print('Error: connective "%s" with %d arguments.' %
                        (expression.connective[0], len(expression.subexpressions)))
            return 0

    elif expression.connective[0].lower() != 'and' and \
         expression.connective[0].lower() != 'or' and \
         expression.connective[0].lower() != 'xor':
        print('Error: unknown connective %s.' % expression.connective[0])
        return 0

    for subexpression in expression.subexpressions:
        if not valid_expression(subexpression):
            return 0
    return 1


def valid_symbol(symbol):
    """Returns whether the given symbol is valid according to our rules."""
    if not symbol:
        return 0

    for s in symbol:
        if not s.isalnum() and s != '_':
            return 0
    return 1

# End of ported code
#-------------------------------------------------------------------------------

# Add all your functions here

#def checkplogic(exp,model):


        #for j in i:
            #if j.symbol[0]:
             #   symbols.append(.symbol[0])

def eval(expression,model):
    if expression.connective[0]=='and':
        #for sub in expression.subexpressions:
        #    if eval(sub,model)==True:
        #        return True
        #return False
        for i,sub in enumerate(expression.subexpressions):
            if i==0:
                #print(i,sub)
                #h=input("first") 
                val=eval(sub,model)
                continue;
            #h=input("frf")
            val=val and eval(sub,model)
        return val
    elif expression.connective[0]=='or':
        for i,sub in enumerate(expression.subexpressions):
            if i==0:
                val=eval(sub,model)
                continue;
            val=val or eval(sub, model)
        return val
    elif expression.connective[0]=='not':
        return not eval(expression.subexpressions[0],model)
    elif expression.connective[0]=='xor':
        for i, sub in enumerate(expression.subexpressions):
            if i==0:
                val=eval(sub, model)
                continue;
            val=(val and not eval(sub,model)) or (not val and eval(sub,model))
        return val
    elif expression.connective[0]=='if':
        return  (not eval(expression.subexpressions[0],model)) or eval(expression.subexpressions[1],model)
    elif expression.connective[0] == 'iff':
        return (eval(expression.subexpressions[0],model) and eval(expression.subexpressions[1],model))
     
    return model[expression.symbol[0]]
 
  
        
def extend(sym,val,m):
    m[sym]=val
    return m


def ttcheckall(kb,a,sym,m):
    #print("Enterdde")
    #print(kb,alpha,model)
    if not sym:
    
        aa=eval(kb,m)
        #print(aa)
        #print(m)
        if aa:

            bb=eval(a,m)
           # print(bb)
            return bb
        else:
            return True
    else:
        s=sym[0]
        r=sym[1:]
        return ttcheckall(kb,a,r,extend(s,True,m)) and ttcheckall(kb,a,r,extend(s,False,m))




def ttentails(knowledgebase, statement, model):
   # print(model)
   # j=input("K")

    s=[]
    n='(not '+statement+')'
    statement=read_expression(statement)
    if not valid_expression(statement):
        sys.exit('invalid statement')

    # Show us what the statement is
    print '\nChecking statement: ',
    print_expression(statement, '')
    print
    #print (statement)

    
    
    #loading symbols.
    getsym(s,knowledgebase,statement)
    s=list(set(s))
  #  print(s)
    
    #for i in range(len(sym)):
    #    kb.append(sym[i])


    symbols=copy.deepcopy(s)
    #print(symbols)
    print("Result:")
    for i in model.keys():
       symbols.remove(i)
   # print(symbols)

    counter=[0]
    nst=read_expression( n,counter)
    true=ttcheckall(knowledgebase, statement, symbols, model)
    false=ttcheckall(knowledgebase, nst, symbols, model)
    
    output=open('result.txt','w')


    if true==True and false==False:
        print("Definitely True.") 
        output.write('Definitely True.')
    elif true==False and false==True:
        print("Definitely False.")
        output.write('Definitely False.')
    elif true==False and false==False:
        print("Possibly True, Possibly False.")
        output.write('Possibly True Possibly False.')
    else:
        print("Both True and False.")    
        output.write('Both True and False.')
    print("Please check results file.")
    output.close()


def effi(subexpression,f,symbols):
    # if f==0:
   pass
