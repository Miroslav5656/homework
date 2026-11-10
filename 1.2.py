a=[2,5,8,11,14,18,21,25,30]
b=18 
c=0
r=-1
h=len(a)-1
while c<=h:
    mid=(c+h)//2
    if a[mid]==b:
        r=mid
        break
    elif a[mid]<b:
        c=mid+1
    else:
        h=mid-1
print(r)