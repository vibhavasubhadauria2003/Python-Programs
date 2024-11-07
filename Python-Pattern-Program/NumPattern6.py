#     1
#    121
#   12321
#  1234321
# 123454321
#  1234321
#   12321
#    121
#     1

n=int(input("Enter limit "))

for i in range(1,n+1,1):
    print(" "*(n-i),end="")
    for j in range(1,i+1,1):
        print(j,end="")
        k=j
    for j in range(i-1,0,-1):
        print(j,end="")
    print()
for i in range(1,n,1):
    print(" "*i,end="")
    for j in range(1,n+1-i,1):
        print(j,end="")
        k=j
    for j in range(n-i-1,0,-1):
        print(j,end="")
    print()