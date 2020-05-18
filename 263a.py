matrix = []
result=0
for i in range(5): 
    matrix.append(list(map(int,input().split(' '))))
for i in range(5):
    for j in range(5):
        if(matrix[i][j]==1):
            x=abs(i-2)
            y=abs(j-2)
            result=x+y
            
print(result)
