a=list(input())
c={'@'}

for i in range(len(a)):
    c.add(a[i])

if((len(c)-1)%2==0):
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')

