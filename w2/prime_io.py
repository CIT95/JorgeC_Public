#jan-20-2021 : Displaying prime number from a number-range entered
print('Hi, please enter a starting number [integers only]')
istart = int(input())
print('Now, the ending number. ')
iend = int(input())
if istart<iend:  
  for i in range(istart,iend+1):
    bPrime = True  
    for inum in range(2,i):
      if (i % inum) == 0:
          bPrime = False
    if (bPrime)and(i!=1):      #excluding 1 since it's not prime
      print('Prime #: '+str(i))
else:
  print('Ending number must be greater than the Starting number')
print('END.')
  