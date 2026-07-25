


#EVEN NUMBERS
a=int(input())
b=int(input())
if a>b:
    print("INVALID RANGE")
else:
    for i in range(a,b+1):
         if(i%2==0):
             
              print(i,end=" ")