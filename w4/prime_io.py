#jan-20-2021 : Displaying prime number from a number-range entered
#program 2 for week4. Implementing try except
def process():
    print('')
    bflag = True
    while bflag:
        print('Hi, please enter a starting number [integers only]: ',end='')
        try:
           istart = int(input())
        except ValueError:
           print('You did not enter a number')    
        else:
            bflag=False   
    
    bflag = True
    while bflag:
        print('Now, the ending number: ',end='')
        try:
           iend = int(input())
        except ValueError:
           print('You did not enter a number')    
        else:          
            bflag=False   
           

    if istart < iend:  
     for i in range(istart,iend+1):
       bPrime = True  
       for inum in range(2,i):
         if (i % inum) == 0:
            bPrime = False
       if (bPrime)and(i!=1):      #excluding 1 since it's not prime
           print('Prime #: '+str(i))
    else: #first if
      print('Ending number must be greater than the Starting number')



bflag = True
while bflag:
    process()
    print('Run it again [y/n]? ',end='')
    if (input()=='n'):
        print('bye')
        bflag = False


