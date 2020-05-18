x,y=map(int,input().split())
c=0
wx=x
wy=y

while(not wx>wy):
    wx=wx*3
    wy=wy*2
    c+=1
    
print(c)
