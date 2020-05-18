a=int(input())
td=[]
resl=[]
for i in range(a):
    x=input().split()
    td.append(int(x[0]))
    td.append(int(x[1]))

for j in range(1,len(td),2):
    if(j==1):
        resl.append(td[1])
    else:
        x=resl[-1]+td[j]-td[j-1]
        resl.append(x)

print(max(resl))
    
