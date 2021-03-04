#https://pynative.com/python-string-exercise/
#https://www.w3resource.com/python-exercises/string/
#saw solution
#case 2 Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1
s1 = 'Ault'
s2 = 'Kelly'
def case2():
    middle=int(len(s1)/2) #we get the middle pos
    end=len(s1)           #end of string index
    print(s1[0:middle]+s2+s1[middle:end])
case2()

#Arrange string chars such that lower case letter should come first
def case4(sval):
    slow=''
    sup='' 
    for i in sval: #i googled the for statement
        if i.islower() == True:
            slow=slow+i
        else:
            sup=sup+i
    return slow+sup        
print(case4('PyNaTive'))

#Count all lower case, upper case, digits, and special symbols from a given string
#saw the solution
def case5(sval):
    schar=0
    ssymbol=0
    idigits=0    
    for i in sval: #i googled the for statement
        if i.isnumeric() == True:
            idigits+=1
        elif i.isalpha() == True:
            ssymbol+=1
        else:
            schar+=1
    return schar,ssymbol,idigits
schar,ssymbol,idigits=case5('P@#yn26at^&i5ve') #https://linuxhint.com/return_multiple_values_python_function/
print('\nCase 5')
print('Chars:   '+str(ssymbol))
print('Digits:  '+str(idigits)) #ok
print('Symbols: '+str(schar))

#https://pynative.com/python-string-exercise/
#Given two strings, s1 and s2, create a mixed String
#saw the solution
def case6(s1,s2):
  s2 = s2[::-1]
  lengthS1 = len(s1)
  lengthS2 = len(s2)
  length  = lengthS1 if lengthS1 > lengthS2 else lengthS2 
  resultString=''
  for i in range(length):
    if(i < lengthS1):
      resultString = resultString + s1[i]
    if(i < lengthS2):
      resultString = resultString + s2[i]    
  return resultString

s1='Abc'  
s2='Xyz'
print(case6(s1,s2))   #AzbycX

#string character balance test
#finding a coincidence within another string
#I tried to do also this one, but needed an array to compare
#looking at the solution, it seems Python is sooo powerful
def case7(s1,s2):
    flag = True
    for i in s1:
        if i in s2:
           continue
        else:
            flag = False
    return flag
s1='tree'
s2='Forest and trees are amazing'
print('String to find: '+s1+'. in '+s2)
if case7(s1,s2)==True:
    print('string was found')
else:
    print('string was not found') 

#Given a string, return the sum and average of the digits that appear in the string, ignoring all other characters
#I did it by myself
def case9(s1):
    snum=''
    itot=0
    for i in s1: #i googled the for statement
      if i.isnumeric() == True:
          snum=snum+i
      else:
          if snum != '': #there is data
            itot=int(snum)+itot    
            snum=''
      
    if snum != '': #there is data
       itot=int(snum)+itot            
    return str(itot)

print(case9('Hola77and34'))
print(case9('Hola77and34bye'))


#Given an input string, count occurrences of all characters within a string
#I was gonna do this by myself but it requires arrays, old fashion programming
#so I decided to see the solution, ohh this is beautiful and powerful
def case10(s1):
    newdict = dict()
    for i in s1:
        itot=s1.count(i)
        newdict[i]=itot
    print(newdict)    
    return newdict

case10('ApPle') #{'A': 1, 'p': 1,'P': 1 'l': 1, 'e': 1}

#Find the last position of a substring “Emma” in a given string
#used https://www.pythonpool.com/python-find/
def case12(s1,s2):
    return s1.rfind(s2)

idx=case12('Emma is a data scientist who knows Python. Emma works at google.','Emma')    
print('Case 12')
print('Last position is: '+str(idx))

#Split a given string on hyphens into several substrings and display each substring
#Used https://www.pythonforbeginners.com/dictionary/python-split
def case13(s1,s2):
    ssub=s1.split(s2)
    for char in ssub:
        print(char)
print('\nCase 13#')
case13('Emma-is-a-data-scientist','-')

#Remove empty strings from a list of strings
#saw the solution
def case14(slist):
    return list(filter(None,slist))   

print(case14(['Emma','Jon','','Kelly',None,'Eric','']))