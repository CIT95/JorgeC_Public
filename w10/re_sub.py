#video 28 https://www.udemy.com/course/automate/learn/lecture/3470530#overview
"""
The sub() regex method will substitute matches with some other text.
Using \1, \2 and so will substitute group 1, 2, etc in the regex pattern.
Passing re.VERBOSE lets you add whitespace and comments to the regex string passed to re.compile().
If you want to pass multiple arguments (re.DOTALL , re.IGNORECASE, re.VERBOSE), combine them with the | bitwise operator.
"""
import re
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))
print(namesRegex.sub('REDACTED','Agent Alice gave the secret documents to Agent Bob.'))

namesRegex = re.compile(r'Agent (\w)\w*') #returning [A,B]
print(namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.'))
print(namesRegex.sub(r'Agent \1****','Agent Alice gave the secret documents to Agent Bob.'))

namesRegex = re.compile(r'''
(\d\d\d)-| #are code without parens, diwht dash
(\(\d\d\d) ) #area code
\d\d\d\d     #first 3 digis
-            #second dash
\d\d\d\d     #last 4 digtss
\sx\d{2,4} # extension.like x1234  ''',re.IGNORECASE | re.DOTALL|re.VERBOSE)
print(namesRegex.findall('668-265-45478 Agent Alice gave the secret documents to Agent Bob.'))