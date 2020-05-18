a=int(input())
p=[]
c=0
for i in range(a):
    x=input()
    p.append(x)
for q in p:
    x=map(int,q.split())
    if(sum(x)>=2):
        c+=1
print(c)
