def binarysearch(list,l,r,x):
    while r>=l:
       mid=(r-l)//2
       if list[mid]==x:
           print(True)
           break
       elif list[mid]<x:
           r=mid
       else:
           l=mid+1
    print(-1)
list=[1,2,3,4,5,6,7,8,9]
l=0
r=len(list)-1
x=int(input("enter the number"))
binarysearch(list,l,r,x)

