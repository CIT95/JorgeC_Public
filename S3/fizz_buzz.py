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

print('Enter a number: ',end='')
inumber = int(input())
print(fizz_buzz(inumber))
