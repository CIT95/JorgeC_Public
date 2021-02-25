

#cansodas = {'coke':1.25,'pepsi':1.21,'fanta':0.99}
sodas = {'name':'coke','price':1.25}

#adding a key to the DD
#https://www.geeksforgeeks.org/python-add-new-keys-to-a-dictionary/
sodas.update({'size':'can'}) 

#sorting the dd
sort_sodas = sorted(sodas.items(),key=lambda x:x[0])
print(sort_sodas)
#diff way to sort it
sort_sodas2 = sorted(sodas.items())
print(sort_sodas2)


#check if a key already exist in a dd
print(sodas.get('price',0))
print(sodas.get('oz',0)) #since OZ don't exist then zero
  
#iterate the dd using loops
print('\nUsing Loops\n')
for k,v in sodas.items(): #loop to show key and value per line
     print(k,v)
print('')
for k in sodas.items(): #showing the items of the dictionary
     print(k)     

#sorting the dd
sodas = {'price':1.25,'oz':12,'ml':365}
sort_sodas = sorted(sodas.items(),key=lambda x:x[1])
print(sort_sodas)
sort_sodas2 = sorted(sodas.items())
print(sort_sodas2)

#filter the dd based onvalues
#will show only sodas greater equal than $1
#https://stackoverflow.com/questions/45037977/get-the-type-of-the-key-of-a-dictionary
print('filte based on values')
for lval in sodas.values():
        print(lval)

#take your dd and create a list of dd
sodas_lst =[ {'name':'coke','price':1.25,'size':'can'},
             {'name':'fanta','price':1.08,'size':'can'},
             {'name':'sprite','price':1.17,'size':'can'},
             {'name':'dew','price':1.12,'size':'can'}]
#https://stackoverflow.com/questions/9152431/iterating-over-list-of-dictionaries
#printing only all the names from the dictionary
lst = [li['name'] for li in sodas_lst]
print(lst)
#printing the entire dictionary
for key in sodas_lst:
     print(key)

#Max
ages = {'Joe':25,'Ron':22,'Bill':36}
#https://tutorialdeep.com/knowhow/key-maximum-value-dictionary-python/
maxval = max(ages,key=ages.get)
print('The MAX age is:')
print(maxval)

#MIN
#https://www.geeksforgeeks.org/python-minimum-value-keys-in-dictionary/
minval = min(ages.values())
print('the MIN value is')
print(minval)

#Average
#https://stackoverflow.com/questions/29664829/can-anyone-help-me-with-finding-the-average-of-dictionary-python-2-7
def CalcAverage(): #the function will get count the total of items
    total = 0.0    #total of value and divide it
    numPersons = 0
    for key,value in ages.items():
        numPersons += 1
        total += float(value)
    return total/numPersons
print(CalcAverage())

#Sum 
print(sum(ages.values()))