a=input("enter the numbers").split(", ");
b=[]
for i in range(0,len(a)):
    b.append(int(a[i]))


for i in b:
    if(i==237):
        break
    elif(i%2==0):
        print(i)
    
