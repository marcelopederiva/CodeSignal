def makeArrayConsecutive2(statues):
  statues.sort()
  menor = statues[0]
  count = 0
  for i in range(1,len(statues)):
    while statues[i] != menor+1:
      menor += 1
      count += 1
    menor +=1
  return count
