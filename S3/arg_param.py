#creating more functions with arguments/parameters
def ToCelcius(ivalue,inum): #ivalue=0 by default in case is none/null        
    celsius = (ivalue - inum) * (5/9)
    return (celsius)

def FullName(sfirst,slast,smess='Good morning!'): #passing arguments(variables)
    return smess+' '+sfirst+' '+slast

bflag = True
while bflag:
  print('Convert Farenheit to Celsius. Enter number: ',end='') 
  print(ToCelcius(int(input()),32)) #passing parameters(values)

  print('Enter your First Name: ',end='')
  svalue1=input()
  print('Enter your Last Name: ',end='')
  svalue2=input()
  
  FullNamesvalues = FullName(svalue1,svalue2)
  print(FullNamesvalues)

  print('Run it again [y/n]? ',end='')
  if (input()=='n'):
      print('bye')
      bflag = False
