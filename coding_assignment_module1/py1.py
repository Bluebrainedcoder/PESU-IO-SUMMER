a=input("enter the numbers").split(",");
b=[]
for i in range(0,len(a)):
    b.append(int(a[i]))

print(a,b);
c=tuple(b)
print(c)
