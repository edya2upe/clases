def count(a):
  total = 0
  return countr(a, total)

def countr(a, total=0):
    if(len(a) == 0):
        return 0
    else:
        total = total + 1
        a.pop()
        countr(a, total)
        return total

print countr([1,2,3,4,5,6,7,8,9,10])
