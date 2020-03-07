# Compute root square
def sqrt(n):
    return n**.5

# Search divisors
def divisors(n):
    divs = [1]
    for i in range(2,int(sqrt(n))+1):
        if i!=n and n%i == 0:
            divs.extend([i,int(n/i)])
    divs.extend([n])
    return sorted(list(set(divs)))

# Sum divisors
def sum_divisors(divs):
  s = 0
  for d in divs:
    s += d

  return s
