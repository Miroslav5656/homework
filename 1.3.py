lst=[29,10,14,37,13]
n=len(lst)
for i in range(n-1):
  mn=i
  for j in range(i+1,n):
    if lst[j]<lst[mn]:
      mn=j
  lst[i],lst[mn]=lst[mn],lst[i]
  print(lst)