# Wumpus Rules

The task in this program assignment is to implement, a knowledge base and an inference engine for the wumpus world. First of all, a knowledge base is created (stored as a text file) storing the rules of the wumpus world, i.e., what we know about pits, monsters, breeze, and stench. Second,an inference engine is created, that given a knowledge base and a statement determines if, based on the knowledge base, the statement is definitely true, definitely false, or of unknown truth value.

Language used- Python

## Code structure
1. check_true_false.py

This includes the template that was provided to us to load files and add expressions and subexpressions to our knowledge base.

I did not change much here. I just moved the creating the statement expression part to the other file.


2. logical_expression.py

### getsym()
Used to get the symbols in knowledge base and statement.

### eval()
Evaluates the expression to use the connective to perform specified operation.
Here I'm applying the connective to each subexpression by calling the function recursively.

### extend()
Simply extends (adds to) the model which has the boolean values for each symbol.

### ttcheckall()
Implemented the algorithm provided in the slide.

### ttentails()
Implemented the algorithm provided in the slide.
Used the statement to create a negation of the statement.
Calling ttcheckall() which in turn calls eval() and evaluates the truth and false values for each expression. 

Input Files- statement1.txt,statement2.txt
Knowledge Base- wumpus_rules.txt
Additional Knowledge Base- additional_knowledge.txt

Usage-
**python check_true_false.py wumpus_rules.txt [additional_knowledge.txt] [statement.txt]**

Example-
python check_true_false.py wumpus_rules.txt additional_knowledge.txt statement1.txt

Loading wumpus rules...
Loading additional knowledge...
Loading statement...

Checking statement: B_1_1
Result:
Definitely False.
Please check results file.
