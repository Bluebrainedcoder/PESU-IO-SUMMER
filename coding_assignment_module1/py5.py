a=input("enter the string")
d=0
for i in a:
    if(i>'0' and i<'9' and d<=1 ):
        p=1
    elif(i=="."):
        d+=1;
    else:
        p=-1
        break
    

if(p==-1):
    print("the string is not an numeric")
else:
    print("the string is an numeric")
