#jan-20-2021 : looping between 2 numbers and displaying them
print('Hi, please enter a starting number [integers only]')
istart = int(input())
print('Now, the ending number. I will output the range entered')
iend = int(input())
if istart<iend:
  for i in range(istart,iend+1):
    print('Value: '+str(i))
else:
  print('Ending number must be greater than the Starting number')
print('END.')
  