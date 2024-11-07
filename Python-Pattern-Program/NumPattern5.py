#     1
#    12
#   123
#  1234
# 12345
#  1234
#   123
#    12
#     1

n=int(input("Enter limit "))

for i in range(1,n+1,1):
    print(" "*(n-i),end="")
    for j in range(1,i+1,1):
        print(j,end="")
    print()
for i in range(1,n,1):
    print(" "*i,end="")
    for j in range(1,n+1-i,1):
        print(j,end="")
    print()