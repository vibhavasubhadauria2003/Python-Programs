# 12345
# 1234
# 123
# 12
# 1

n=int(input("Enter limit"))

for i in range(1,n+1,1):
    for j in range(1,(n+2)-i,1):
        print(j,end="")
    print()

