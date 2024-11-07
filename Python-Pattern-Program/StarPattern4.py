#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

n=int(input("Enter limit"))
for i in range(1,n+1,1):
    print(" "*(n-i)+"*"*(2*i-1))
for i in range(1,n,1):
    print(" "*i+"*"*((n-i)*2-1))