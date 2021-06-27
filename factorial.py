from functools import reduce

def factorial(n):
   return reduce(lambda i,j: i*j, range(1,n+1)) 

print(factorial(10))
