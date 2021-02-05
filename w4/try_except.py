#program 2 for week4
def divide():
    print('')
    bflag = True
    while bflag:
        print('Enter a number (Dividend): ',end='') 
        try:
           ix = int(input())
        except ValueError:
           print('You did not enter a number')    
        else:
            bflag=False   
    
    bflag = True
    while bflag:
        print('Enter a number (Divisor): ',end='') 
        try:
           iy = int(input())
        except ValueError:
           print('You did not enter a number')    
        else:          
            bflag=False   
           

    try:
        result = ix / iy
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("Result will be float.")


bflag = True
while bflag:
    divide()
    print('Run it again [y/n]? ',end='')
    if (input()=='n'):
        print('bye')
        bflag = False


