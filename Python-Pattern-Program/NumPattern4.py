# 54321
# 4321
# 321
# 21
# 1

n=int(input("Enter limit"))

for i in range(1,n+1,1):
    for j in range((n+1)-i,0,-1):
        print(j,end="")
    print()
