lst = [12,4,9,1,6,3]
print("Исходный список:",lst)
n=len(lst)
w=1
while w<n:
  for i in range(0,n,2*w):
    lt=lst[i:i+w]
    rt=lst[i+w:i+2*w]
    l=0
    r=0
    k=i
    while l<len(lt) and r<len(rt):
      if lt[l]<=rt[r]:
        lst[k]=lt[l]
        l+=1
      else:
        lst[k]=rt[r]
        r+=1
      k+=1
    while l<len(lt):
      lst[k]=lt[l]
      l+=1
      k+=1
    while r<len(rt):
      lst[k]=rt[r]
      r+=1
      k+=1
  w*=2
print("Отсортированный список:",lst)