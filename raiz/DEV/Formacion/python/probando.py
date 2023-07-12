# Alejandro Ruiz De Prada (Córdoba, Argentina. 2023)

x = 5
y = "hola"
z = 5.6
w = 1j
u = ["apple","banana","mordisco"]
t = ("asco","parametro","comida")
s = range(6)
r = {"name" : "jhon", "age" : 36}
q = {"apple","manzana","Cherry"}
p = frozenset({"apple","banana","cherry"})
o = True
ñ = b"Hello"
n = bytearray(5)
m = memoryview(bytes(5))
l = None




print(type(x))
print(type(y))
print(type(z))
print(type(w))
print(type(u))
print(type(t))
print(type(s))
print(type(r))
print(type(q))
print(type(p))
print(type(o))

print("probando CONVERSION")
num2 = 1 
num3 = complex(num2) # Los "complex numbers" son escritos con una "j" en la "imaginary part"
print(num3)

# probando "Random Module"
import random
print(random.randrange(1,10))

# "strings are Arrays"
arr1 = "Hola mundo"
print(arr1[1])

for x in "banana": # iterando con {for} ; -loop-
    print(x)
    
frase1 = "yo me comprometo"
print(frase1)
print(frase1.upper())
print(frase1)
frase1 = frase1.upper() # de esta manera lo convertimos en {.upper()}
print(frase1)
