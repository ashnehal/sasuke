import sys

""""
n= int(input('enter the number'))

while n>0 :
    r=n%10
    if r>7:
        print("it is not an octal number")
        sys.exit(0) #it just stop the compiling there

    n = int(n/10)
print('it is an octal number')
"""

n= int(input('enter the number :'))

flag=1
while n>0 :
    r=n%10
    if r>7:
        flag=0
        break  #break will terminate loop and execute line which is prrsent out of the loop

    n = int(n/10)

if flag==1:
    print('it is an octal number')

else:
    print("it is not an octal number")