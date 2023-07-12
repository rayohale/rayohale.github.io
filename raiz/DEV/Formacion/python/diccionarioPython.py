# Comentarios
comentario = "#"
comentario_multiple = '""" o ' + "'''"

# operadores aritméticos
suma = "+"
resta = "-"
multiplicación = "*"
división = "/" # devuelve FLOAT
potenciacion = "**"
exponente = "**"
división_baja = "//"
módulo = "%"
resto = "%"

print("Ingrese su consulta")
respuesta = input()
print(respuesta)


####### TUTORIAL W3SCHOOLS

# 6. VARIABLES

    # a) Python variables

        # Declarando (creating) variables
variable = "hola"

        # casting
        # data type (tipo de dato)
datatypeStr = str(3)
datatypeInt = int(3)
datatypeFloat = float(3) 
print(type(datatypeInt))

        # single and doble qoutes
        # case-sensitive camelCase

    # b) Variable Names      
''' 
    A variable name must start with a letter or the underscore character
    A variable name cannot start with a number
    A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    Variable names are case-sensitive (age, Age and AGE are three different variables)
    A variable name cannot be any of the Python keywords.
'''

        # ilegal variable names
''' 
            2myvar =
            my-var =
            my var = 
'''
        
        # camelCase 
        # PascalCase
        # snake_case
        
    # c) Assign multiple values
        # many values to multiple variables
mvA, mvB, mvC = "A", "B", "C"
        # one value to multiple variables
ovA = ovB = ovC = "One Value to Multiples variables"
        # unpack a collection
fruits = ["apple", "pera", "manzana"]
x, y, z = fruits

    # d) output variables
        # output variables
print(x, y, z)
print(x + y + z)
print(datatypeFloat + datatypeInt)
        # if you try to combine str ant int/float, PYTHON return 'error'
    # e) global variables
        # if you create a new variable inside a function, with the same name of other variable; it will be LOCAL.
        # to create a global variable inside a function, you can use GLOBAL heyword
def miFun():
        global x
        x = "fantastic"
        
miFun()

print("Python is " + x)

        # also you can change the value of a VARIABLE inside a FUNCTION, using GLOBAL keyword

# 7. DATA TYPES

""""
        Text type:      str             → "Hello world"         (texto)
        Numeric types:  int             → 3                     (enteros)
                        float           → 5.6                   (decimales)
                        complex         → 1j                    (número+letra)
        Sequence types: list            → ["apple","banana"]    (lista)
                        tuple           → ("apple", "banana")   (lista, ordenada e incambiable)
                        range           → range(5)              (función)
        Mapping tyoe:   dict            → {"name": "Juan", "edad" : 32} (diccionario)
        Set types:      set             → {"pera", "mono",..}   (set?)
                        frozenset       → frozenset({"apple", "pera"}) (..)
        Boolean type:   bool            → True
        Binary types:   bytes           → b"Hello"              (..)
                        bytearray,      → bytearray(5)          (..)
                        memoryview      → memoryview(bytes(5))  (..)
        None type:      NoneType        → None                  (Nada)
"""
        
"""
        ### Setting the specific Data type
        x = srt("Hello world")
        ...
        list(("apple", "banana"))
        tuple(("apple","banana"))
        range(6)
        dict(name="Hale", age=31)
        set(("apple","banana"))
        frozenset(("apple", "banana"))
        bool(5)
        bytes(5)
        bytearray(5)
        memoryview(bytes(5))
"""

# 8. NUMBERS
num1 = 1        # int
num2 = 2.8      # float
num3 = 1j       # complex
num4 = complex(num1) # al convertirlo en complex, le va a agregar un +0j al final

        # Random Number
"""
        import random
        print(rando.randrange(1,10))
"""
###########

# 9. CASTING (fundición)
        # es cuando le damos un specify type a una variable
        # "constructor functions" → es lo que hice con "num4" más arriba
###########

# 10. STRINGS

        # (a) : Strings →  "" & '' sirven para setear un string,

# MULTIPLE STRINGS
str1 = """También se puede setear una 'multiline string', con triple comillas .. acá tenemos una multilinea, una cadena miultilinea,
podríamos seguir escribiendo abajo
y componer toda una frase entre estas tres comillas""" 

# STRINGS ARE ARRAYS
print(str1)
print(str1[9]) # Recordar la existencia de la posición [0]
print("Arriba tendría que estar la letra 'e'")

# LOOP
                # we can also "loop" through the characters in a STR with {for} loop.
"""
for x in "banana":
        print(x)
"""

# len()
print(len(str1)) # → 'len()' nos dará la longitud (length) de la [str]

# {in}
print("También" in str1) # {in} ; Check → {"" in x} 
if "También" in str1: # también podemos usar {if}
        print("Sí, 'También' está presente en 'str1'") 

# {not in}
print("seguir" not in str1)


        # (b) : Slicing strings
print(str1[2:7])        # SLICING
print(str1[:5])         # FROM THE START
print(str1[10:])        # TO THE END
print(str1[-10:-2])     # NEGATIVE INDEXING → start from the end

        # (c) : Modify strings
print(str1.upper())     # .upper() : UPPER CASE → convierte en mayúsculas
print(str1.lower())     # .lower() : LOWER CASE → convierte en minúsculas
str2 = "  Doble espacio antes y después  "
print(str2.strip())     # .strip() : REMOVE WHITESPACE → espacio pre y post del [str]

        







####### str a variable

# usando exec()
""" 
name = 'Elon'
exec("%s = %d" % (name = 100))
print(Elon)
"""
# usando locals()
"""
user_input = input("Enter string... \n")
locals()[user_input] = 50
print(apple)
print(type(apple))
"""

#usando globals()
user_input = input("Enter string 'apple' or this prog output ERROR..")
globals()[user_input] = 50
print(apple)
print(type(apple))

