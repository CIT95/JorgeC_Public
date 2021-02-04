#Enhancing this program using TRY EXCEPT
#using functions and returning a value,int and ret string
def fizz_buzz(inumber):
    if (inumber % 3 == 0) and (inumber % 5 == 0):
        return 'FizzBuzz'
    elif inumber % 5 == 0:
        return 'Buzz'
    elif inumber % 3 == 0:
        return 'Fizz'    
    else:
        return inumber

bflag = True
while bflag:
  print('Enter a number: ',end='') 
  try:
      inumber = int(input())
  except ValueError:
      print('You did not enter a number')    
  else: 
      print(fizz_buzz(inumber))
  finally:
      print('Run it again [y/n]? ',end='')
      if (input()=='n'):
        print('bye')
        bflag = False


#end of it
