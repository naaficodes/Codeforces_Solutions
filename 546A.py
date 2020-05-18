k,n,w=map(int,input().split())
x=0
for i in range(1,w+1):
        x+=i*k
    
if(x>n):
    print(abs(n-x))
else:
   print(0)
