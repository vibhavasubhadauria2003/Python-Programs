n=int(input("Enter limit of squre matrix : "))
def printMatrix(m):
    for item in m:
        for item1 in item:
            print(item1,end=" ")
        print()
def inputMatrix(n):
    m=[]
    for i in range(n):
        m0=[]
        print(f'=>Enter items of row number {i+1}')
        for j in range(n):
            x=int(input("   Enter item : "))
            m0.append(x)
        m.append(m0)
    return m
def matrixMul(m1,m2,n):
    mult=[]
    for i in range(n):
        temp=[]
        for j in range(n):
           # temp.append(m1[i][0]*m2[0][j]+m1[i][n-1]*m2[n-1][j])
            sum=0
            for k in range(n):
                  sum+=m1[i][k]*m2[k][j]
            temp.append(sum)
        mult.append(temp)

    return mult


print("Enter First matrix")
m1=inputMatrix(n)
print("Enter Second matrix")
m2=inputMatrix(n)
print("First matrix")
printMatrix(m1)
print("Second matrix")
printMatrix(m2)

print("Multiplied matrix is")
mMult=matrixMul(m1,m2,n)
printMatrix(mMult)