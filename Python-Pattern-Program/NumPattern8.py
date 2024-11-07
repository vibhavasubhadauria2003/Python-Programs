# 1*2*3*10*11*12
#   4*5*8*9
#     6*7

n=int(input("Enter limit "))
k=1
l=0
for m in range(n,0,-1):
    l=l+m
l=l*2
l=l-n+1

for i in range(1,n+1,1):
    x=l
    print("  "*(i-1),end="")
    for j in range(1,n+2-i,1):
        print(k,end="")
        k+=1
        print("*",end="")
    for j in range(1,n+2-i,1):
        print(x,end="")
        x+=1
        if j<(n+1-i):
            print("*",end="")
    l=l-(n-i)    
    print()
