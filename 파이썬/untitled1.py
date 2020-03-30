A = [[3,1,-1],[1,4,1],[2,1,2]]
b = [2,12,10]
x = [0,0,0]

n=3

for i in range(n-1) :
    for k in range(i+1,n) :
        piv = -A[k][i]/A[i][i]
        for j in range(i+1,n) :
            A[k][j]=A[k][j]+piv*A[i][j]    
        b[k]=b[k]+piv*b[i]

print(A)
print(b)        

A[1][0], A[2][0], A[2][1] = 0, 0, 0
x[n-1] = b[n-1]/A[n-1][n-1]
for i in range(n-2,-1,-1) :
    xsum = 0
    for k in range(i+1,n) :
        xsum = xsum + A[i][k]*x[k]
    x[i]=(b[i]-xsum)/A[i][i]

print(x)