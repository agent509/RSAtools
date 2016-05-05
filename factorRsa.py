from math import *


def mysqrt(n):
  x = n
  y = (x + 1) // 2
  while y < x:
    x = y
    y = (x + n // x) // 2
  return x

def factor(N,iter):

  a = 0 
  perfect = False

  while not perfect:

    if a>= iter:
      print("Error, iter exceeded, no factors found.")
      return -1,-1

    a = a+1
    b_sqrd = N+a*a 
    b = mysqrt(b_sqrd)

    if b**2 == b_sqrd:
      perfect = True


  return(b-a,b+a)



def main():
  N = int(input("Enter number to factor: "))
  iter = int(input("Enter maximum number of factoring attempt: "))

  print("Here are the factors of N:",factor(N,iter))
  return 0

main()
