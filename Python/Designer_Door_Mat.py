# Enter your code here. Read input from STDIN. Print output to STDOUT\

def rangoli(value):
  value =value.split()
  m=int(value[0])
  n= int(value[1])
  a= int((m-1)/2)
  c= int((n-7)/2)
  for i in range(a):
      print( ('-')*((a*3)-(i*3))+('.|.')*(2*i+1) + ('-')*((a*3)-(i*3)))
    
  print(('-')*(c)+ 'WELCOME' +('-')*(c))

  for i in range(a):
      print( ('-')*((i*3+3)) +('.|.')*((2*a)-(2*i+1)) + ('-')*((i*3+3)))

if __name__=='__main__':
  s=rangoli(input())      
      

''' This code print pattern like this, try for 7 21, 11 33 or you can try for any odd number
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
'''      