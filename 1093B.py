n=int(input())
ipl={}
result=[]

def pali(x):
    y=x[::-1]
    if(x==y):
        return 1
    else:
        return 0

"""        
def rearre(x):
    y=list(x)
    ll=len(y)
    for i in range(0,ll-1,2):
        xi=y[i]
        yi=y[i+1]
        y[i]=yi
        y[i+1]=xi
    return ''.join(y)
"""


def rearre(x):
    y=list(x)
    y.sort()
    return ''.join(y)


   
for i in range(n):
    x=input()
    if((len(x)==1) or (pali(rearre(x))==1)):
        ipl[x]=-1
    else:
        ipl[x]=pali(x)


for i in ipl:
    if(ipl[i]==1):
        result.append(rearre(i))
    elif(ipl[i]==0):
        result.append(rearre(i))
    elif(ipl[i]==-1):
        result.append(-1)


for result in result:
    print(result)



