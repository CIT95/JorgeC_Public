#https://www.udemy.com/course/automate/learn/lecture/3470522#content
#video 27
"""
The regex method findall() is passed a string, and returns all matches in it, not just the first match.
If the regex has 0 or 1 group, findall() returns a list of strings.
If the regex has 2 or more groups, findall() returns a list of tuples of strings.
\d is a shorthand character class that matches digits. \w matches "word characters" (letters, numbers, and the underscore). \s matches whitespace characters (space, tab, newline).
The uppercase shorthand character classes \D, \W, and \S match charaters that are not digits, word characters, and whitespace.
You can make your own character classes with square brackets: [aeiou]
A ^ caret makes it a negative character class, matching anything not in the brackets: [^aeiou]
"""


import re
beginswithhelloRegex = re.compile(r'^Hello')
print(beginswithhelloRegex.search('Hello there'))

beginswithhelloRegex = re.compile(r'world!$') #find the word and $ means at the very end
print(beginswithhelloRegex.search('Hello world!'))

beginswithhelloRegex = re.compile(r'world!$') 
print(beginswithhelloRegex.search('Hello world!aesdfasdfasd')) #won't be found

print('^\d+$')
alldigitsRegex = re.compile(r'^\d+$')
print(beginswithhelloRegex.search('123132564654')) 
print(beginswithhelloRegex.search('123132x564654')) 

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat'))
atRegex = re.compile(r'.{1-2}at')
print(atRegex.findall('The cat in the hat sat on the flat mat'))

print('.*')
nameRegex = re.compile(r'First Name: (.*) Last Name (.*)')
print(nameRegex.findall('First Name: Albert Last Name: Collins'))

print('<(.*?)>')
nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall('<To serve humans> for dinner.>'))

print('<(.*)>')
nongreedy = re.compile(r'<(.*)>')
print(nongreedy.findall('<To serve humans> for dinner.>'))

print('.*')
nongreedy = re.compile(r'.*')#any char except \n
print(nongreedy.findall('Serve the public trust.\nProtect innoncents.\nUpload the law.'))

print('.*,re.DOTALL')
nongreedy = re.compile(r'.*',re.DOTALL)#any char except \n, including \n
print(nongreedy.findall('Serve the public trust.\nProtect innoncents.\nUpload the law.'))

print('[a-u]')
vowelRegex = re.compile(r'[aeiou]')
print(vowelRegex.findall('Serve the public trust.Protect innoncents.Upload the law.'))
print('[a-u]')
vowelRegex = re.compile(r'[aeiou]',re.I)#ignores uppercase
print(vowelRegex.findall('Serve the public trust.Protect Innoncents.Upload the law.'))

