n,k=input().split()
s=input().split()
m=s[int(k)-1]
c=0
for x in s:
    if(int(x)>0 and int(x)>=int(m)):
        c+=1
print(c)
