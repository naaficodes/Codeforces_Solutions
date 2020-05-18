x,y=input().split()
res=x


for i in range(int(y)):
        if(res[-1]=='0'):
            res=str(int(res)//10)
        elif(not res[-1]=='0'):
            res=str(int(res)-1)

print(res)

    
