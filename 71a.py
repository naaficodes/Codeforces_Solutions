a=int(input())
def shrt(longword):
    if(len(longword)>10):
       return longword[0]+str(len(longword)-2)+longword[len(longword)-1]
    else:
        return longword
    
for i in range(a):
    x=input()
    print(shrt(x))
    
