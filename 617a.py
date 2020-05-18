a=int(input())
"""c=0
ri=a
for i in range(5,0,-1):
    while(ri-i<ri and ri-i>=0):
        ri-=i
        c+=1
"""
c=0
if(not a%5==0):
    c=(a//5)+1
else:
    c=a//5

print(c)
    
    


