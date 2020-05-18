import math
x,y=input().split()
m=int(x)
n=int(y)
o=0
if((m*n)%2==0):
     o=math.floor((m*n)/2)
elif((m*n)%2!=0):
    o=math.floor(((m*n)-1)/2)
print(o);
