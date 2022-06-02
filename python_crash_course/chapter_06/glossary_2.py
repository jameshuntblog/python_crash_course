# glossary_2.py

glossary = {'argument':'Argument or arg is a value that is passed into a'\
    ' command or a function. For example, if SQR is a routine or function'\
    ' that returns the square of a number, then SQR(4) will return 16. Here,'\
    ' the value 4 is the argument. Similarly, if the edit is a function that' \
    ' edits a file, then in edit myfile.txt, ‘myfile.txt’ is the argument.',
    'Boolean':'A Boolean expression or Boolean logic is an expression used for'\
    ' creating statements that are either TRUE or FALSE. Boolean expressions'\
    ' use AND, OR, XOR, NOT and NOR operators with conditional statements in'\
    ' programming, search engines, algorithms, and formulas. Boolean'\
    ' expressions are also called comparison expressions, conditional'\
    ' expressions, and relational expressions.',
    'braces':'{ is an opening brace and } is a closing brace.}',
    'dictionaries':'Python dictionaries allow you to connect pieces of related'\
    ' information',
    'list':'A list is a data structure in Python that is a mutable, or'\
    ' changeable, ordered sequence of elements.',
    'python':'Python is a high-level, interpreted, general-purpose programming'\
    ' language.',
    'Object-oriented programming':'Object-oriented programming (OOP) is a'\
    ' programming paradigm based on the concept of "objects", which can'\
    ' contain data and code: data in the form of fields (often known as'\
    ' attributes or properties), and code, in the form of procedures (often'\
    ' known as methods).',
    'f-string':'An f-string is a formatted string literal. To write these, we'\
    ' precede a string with the letter ‘f’ or ‘F’. This lets us put in values'\
    ' into a string.',
    'variable':'A variable is a place in computer memory with an assigned'\
    ' name. We need variables to store and retrieve data of different types'\
    ' (text, numbers, etc.). Creating a variable is called "declaring the'\
    ' variable". You name your variable and assign a value to it.',
    'interpreter':'Interpreters run through each line of the program and'\
    ' execute all the commands on the fly. They also verify each line of code'\
    ' to ensure it is written correctly. If the interpreter encounters any'\
    ' errors in the code, it will show a message that includes the type of an'\
    ' error and the place in the code where it occurred.',
    }

for term,defintion in glossary.items():
    print(f"\n{term.title()}:\n\t{defintion}")

