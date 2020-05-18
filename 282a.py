z=int(input())
l=[]
x=0
for i in range(z):
    l.append(input())
    
for o in l:
    if('+' in o):
        x+=1
    elif('-' in o):
        x-=1
print(x)
