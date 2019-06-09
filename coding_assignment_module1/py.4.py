a=int(input("enter the number"))
s=0
while(a>0):
    s+=(a%10)
    a=int(a/10)

print(s)
