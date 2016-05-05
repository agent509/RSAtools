from random import *

#Fast exponentiation algorithm

def fastexp(g,x,n):
  result = 1
  while x!=0:
    if x%2==1:
      result = (result*g)%n
    x=x//2
    g = (g*g)%n

  return(result)



#Miller-Rabin probabilistic primality test

def isPrime(n,k):

  if n%2==0:
    return(False)

  d = n-1
  s = 0
  while d%2==0:
    s=s+1 
    d=d//2
  
  for a in range(k):
    a = SystemRandom().randint(2,n-2)
    x = fastexp(a,d,n)
    doNextLoop = False
    if (x==1 or x==n-1):
      doNextLoop = True
    else:
      for j in range(s-1):
        x=(x*x)%n
        if x==1:
          return(False)
        elif x==n-1:
          doNextLoop = True
          break

    if not doNextLoop:
      return(False)

  return(True)


key = int(input("Enter bitsize of prime number: "))

#Generate a random prime number of specified bitsize
###########
p = SystemRandom().randint(2**(key-1),2**(key+1))
while not isPrime(p,40):
  p = SystemRandom().randint(2**(key-1),2**(key+1))
##############  

#Print prime number
print("p=",p)



#Find and print nearby prime number
flag = False
q=p
q+=2

while(not flag):
  q+=2
  if(isPrime(q,40)):
    flag = True

print("q=",q)
print("n=",p*q)

