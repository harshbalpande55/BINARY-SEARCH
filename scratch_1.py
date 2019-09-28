def binarysearch(list,l,r,x):
  if (r-l)>=0:
    mid=(r-l)//2
    if list[mid]==x:
      print(true)
    if x < list[mid]:
      binarysearch(list, l,mid, x)
    if x > list[mid]:
      binarysearch(list, mid+1,r, x)
  else:
    print(-1)
list=[1,2,3,4,5,6,7,8,9]
l=0
r=len(list)-1
x=int(input())
binarysearch(list,l,r,x)
