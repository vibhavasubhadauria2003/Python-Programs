n=input("Enter the number ")
n=int(n)
a=n
S=0
d=0
while a>0:
    d=a%10
    S=S+(d*d*d)
    a=a//10
if S==n:
    print("Yes it is Armstrong")
else:
    print("nooo...")
