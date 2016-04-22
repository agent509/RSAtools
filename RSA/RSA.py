from random import *
import os

def egcd(a, b):
  x,y, u,v = 0,1, 1,0
  while a != 0:
    q, r = b//a, b%a
    m, n = x-u*q, y-v*q
    b,a, x,y, u,v = a,r, u,v, m,n
  gcd = b
  return gcd, x, y

def modinv(a, m):
  gcd, x, y = egcd(a, m)
  if gcd != 1:
    return None  # modular inverse does not exist
  else:
    return x % m

def fastexp(g,x,n):
  result = 1
  while x!=0:
    if x%2==1:
      result = (result*g)%n
    x = x//2
    g = (g*g)%n
  return(result)

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



def generate(key):
  
  p = SystemRandom().randint(2**(key-1),2**(key+1))
  while not isPrime(p,40):
    p = SystemRandom().randint(2**(key-1),2**(key+1))
  q = SystemRandom().randint(2**(key-1),2**(key+1))
  while not isPrime(q,40):
    q = SystemRandom().randint(2**(key-1),2**(key+1))

  n=p*q
  phin = (p-1)*(q-1)
  e = 65537
  d = modinv(e,phin)
  
  pub = open("public.txt","w")
  pub.write(str(e)+':'+str(n))
  pub.close()

  priv = open("private.txt","w")
  priv.write(str(d)+':'+str(n))


def encrypt(keyfile,message):
  pub = open(keyfile,"r")
  key = pub.readline()
  key = key.split(":")
  e = int(key[0])
  n = int(key[1])
  pub.close()

  mf = open(message,"rb")
  blocksize = (n.bit_length()//8-1)
  m = int.from_bytes(mf.read(blocksize),byteorder="little")
  f = open(message+".enc","w")
  while m!=0:
    c = fastexp(m,e,n)
    f.write(str(c)+'\n')
    m = int.from_bytes(mf.read(blocksize),byteorder="little")

  mf.close()
  f.close()

def decrypt(keyfile,message,output):
  priv = open(keyfile,"r")
  key = priv.readline()
  key = key.split(":")
  d = int(key[0])
  n = int(key[1])
  priv.close()

  f = open(message,"r")
  blocksize = (n.bit_length()//8)-1

  c = (f.readline().strip())
  of = open(output,'wb')
  while c != '':
    m = fastexp(int(c),d,n)
    m = m.to_bytes((m.bit_length()+7)//8,byteorder="little")
    of.write(m)
    c = (f.readline().strip())

  f.close()
  of.close()

def main():
  choice = input("Enter \"g\" for generate, \"e\" for encrypt, or \"d\" for decrypt: ")

  if choice == "g":
    keysize = input("Enter the bit-size of the key to generate: ")
    generate(int(keysize))
  elif choice == "e":
    keypath = input("Enter the path of public key: ")
    message = input("Enter path of message to encrypt: ")
    encrypt(keypath,message)
  elif choice == "d":
    keypath = input("Enter path of private key: ")
    message = input("Enter path of encrypted message: ")
    output = input("Enter path to output: ")
    decrypt(keypath,message,output)
    
  return 0

main()

