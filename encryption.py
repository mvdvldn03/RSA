from random import randint
def isPrime(x):
  if x < 2:
    return False
  elif x == 2:
    return True  
  for n in range(2, x):
    if x % n == 0:
      return False
  return True
def isCoprime(x,y):
  if x < y:
    for n in range(2,x):
      if x % n == 0 and y % n == 0:
        return False
  if y < x:
    for n in range(2,y):
      if x % n == 0 and y % n == 0:
        return False
  return True
def text_code_translator(inp,code,symbol):
  if symbol in inp:
    inp = inp.replace(symbol,code)
    return inp
  else:
    return inp
for x in range(10**3):
  i = randint(10**2,10**3)
  if isPrime(i):
    p = i
    break
for x in range(10**3):
  i = randint(10**2,10**3)
  if isPrime(i) and i != p:
    q = i
    break
n = p*q
totient = (p-1)*(q-1)
max_chars = (int(len(str(n))/2))
for x in range(1000):
  i = randint(2,20)
  if isCoprime(i,totient) and (totient % i != 0):
    e = i
    break
d = min([i for i in range(10**8) if (i*e) % totient == 1])
print("Public Keys:\nn = " + str(n) + " (Max Chars - " + str(max_chars) + ")/e = " + str(e))
plaintext_1 = []
plaintext_2 = []
plaintext_3 = []
ciphertext_1 = []
message = input("\nMessage to be Encrypted")
plaintext_1.append([message[i:i+max_chars-1] for i in range(0, len(message), max_chars-1)])
for item in plaintext_1:
  plaintext_1 = item
for term in plaintext_1:
  term = text_code_translator(term,"10","0")
  term = text_code_translator(term,"11","1")
  term = text_code_translator(term,"12","2")
  term = text_code_translator(term,"13","3")
  term = text_code_translator(term,"14","4")
  term = text_code_translator(term,"15","5")
  term = text_code_translator(term,"16","6")
  term = text_code_translator(term,"17","7")
  term = text_code_translator(term,"18","8")
  term = text_code_translator(term,"19","9")
  term = text_code_translator(term,"20","a")
  term = text_code_translator(term,"21","b")
  term = text_code_translator(term,"22","c")
  term = text_code_translator(term,"23","d")
  term = text_code_translator(term,"24","e")
  term = text_code_translator(term,"25","f")
  term = text_code_translator(term,"26","g")
  term = text_code_translator(term,"27","h")
  term = text_code_translator(term,"28","i")
  term = text_code_translator(term,"29","j")
  term = text_code_translator(term,"30","k")
  term = text_code_translator(term,"31","l")
  term = text_code_translator(term,"32","m")
  term = text_code_translator(term,"33","n")
  term = text_code_translator(term,"34","o")
  term = text_code_translator(term,"35","p")
  term = text_code_translator(term,"36","q")
  term = text_code_translator(term,"37","r")
  term = text_code_translator(term,"38","s")
  term = text_code_translator(term,"39","t")
  term = text_code_translator(term,"40","u")
  term = text_code_translator(term,"41","v")
  term = text_code_translator(term,"42","w")
  term = text_code_translator(term,"43","x")
  term = text_code_translator(term,"44","y")
  term = text_code_translator(term,"45","z")
  term = text_code_translator(term,"46","A")
  term = text_code_translator(term,"47","B")
  term = text_code_translator(term,"48","C")
  term = text_code_translator(term,"49","D")
  term = text_code_translator(term,"50","E")
  term = text_code_translator(term,"51","F")
  term = text_code_translator(term,"52","G")
  term = text_code_translator(term,"53","H")
  term = text_code_translator(term,"54","I")
  term = text_code_translator(term,"55","J")
  term = text_code_translator(term,"56","K")
  term = text_code_translator(term,"57","L")
  term = text_code_translator(term,"58","M")
  term = text_code_translator(term,"59","N")
  term = text_code_translator(term,"60","O")
  term = text_code_translator(term,"61","P")
  term = text_code_translator(term,"62","Q")
  term = text_code_translator(term,"63","R")
  term = text_code_translator(term,"64","S")
  term = text_code_translator(term,"65","T")
  term = text_code_translator(term,"66","U")
  term = text_code_translator(term,"67","V")
  term = text_code_translator(term,"68","W")
  term = text_code_translator(term,"69","X")
  term = text_code_translator(term,"70","Y")
  term = text_code_translator(term,"71","Z")
  term = text_code_translator(term,"72"," ")
  term = text_code_translator(term,"73",".")
  term = text_code_translator(term,"74","'")
  term = text_code_translator(term,"75",",")
  plaintext_2.append(term)
for term in plaintext_2:
  ciphertext_1.append((int(term)**e)%n)
print("\nPrivate Keys:\nd = " + str(d) + "\n")
for term in ciphertext_1:
  plaintext_3.append(str((term**d) % n))
print(ciphertext_1)
print(plaintext_2)
print(plaintext_3)
