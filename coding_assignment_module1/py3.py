a=input("enter the numbers").split(",");
b=[]
for i in range(0,len(a)):
    b.append(int(a[i]))
ele=int(input("enter the element to be searched"));
b.sort()
first=0
last=len(b)-1

p=0
while(first<last):
    mid=int((first+last)/2)
    if(ele==b[mid]):
        print("element found")
        p=1;
        break
    elif(ele<b[mid]):
        last=mid-1
    else:
        first=mid+1
if(p==0):
    print("element not found")
print(b)
