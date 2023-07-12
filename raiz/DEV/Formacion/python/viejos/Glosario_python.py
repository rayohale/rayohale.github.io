#Glosario Python


print("Estos son los apuntes de estudio de Python")
 
"""
### INDICE

1) Numeros
    > todas las operaciones numericas que se introducen, PYTHON las realiza como una computadora
    > '+' , '/' , '-' , '*'
    > las divisiones '/', son devueltas como numeros flotantes (FLOAT: 1.6 , 5.0 , etc)
    > INT se denomina a los numeros enteros sin decimal (5, 6, 20, etc)
    > floor division '//' --> obtendría un numero descartando cualquier decimal
    > '%' --> retorna el RESTO de la operación
    > '**' calcular potencia (5 ** 2 sería cinco al cuadrado)
    > '=' --> ASIGNAR un VALOR a una VARIABLE
    > si una VARIABLE no esta DEFINIDA (con un VALOR ASIGNADO) dará ERROR
    >>> round(N, 2) -> redondea a N con dos decimales
    
2) Cadenas de textos (STRING)
    
    > se usan comillas o " , o '.
    > " \' " -> para "escaparle" a las comillas, por ejemplo 'doesn\'t'
    > también se puede usar "help's"
    > print() [imprime sin comillas, ejemplo: print("hola") >>> hola]
    
    >>> print('El resultado es', 5)
    El resultado es 5
    # Agrega espacio en blanco automaticamente
    # si usamos el parámetro 'end' entonces lo elimina
    >>> print('El resultado es', end=5)
    El resultado es5
    
    >>> \n [salta de linea]
    >>> print(r'hola\nombre') >>> hola\nombre {CADENAS CRUDAS}
    >>> print(
     no se que hacen tres puntitos entremedio de las tres comillas '...'
     todo lo que se escriba en estas tres comillas hay que volver a cerrarlo 
     con parentesis SIN LAS COMILLAS
     lo que si se es que también se puede poner '\' al final de las tres comillas
     que elimina el salto de línea automático SLA
              )
    
    >>> 3 * 'un' 
    ununun
    
    >>> 'un' + 'por' -> unpor
    > CADENAS LITERALES: aquellas cerradas entre comillas
    >>> texto = ('poner muchas cadenas en un parentesis '
                 'para que las una todas juntas después.')
    >>> prefix = 'Py'
    >>> prefix + 'thon'      #Contatenando VARIABLE con un LITERAL
    'Python'
    
    INDEXAR: hacer sub-indices
    
    > el primer carácter de la CADENA tiene el INDICE 0
    >>> prefix[0]
    'P'
    >>> prefix[-1]
    'y'
    >>> palabra = 'Complemento'
    
    REBANADAS:
    >>> palabra[0:3]
    'Com'
    >>> palabra[3:8]
    'plemento'
    >>> palabra[:2] + [2:]
    'Complemeneto'
    # [:2] Incluye // [2:] excluye
    # VALOR por defecto del primer INDICE es '0', y del segundo INDICE
        es la longitud de la cadena
    
    
3) Listas
        
       > es un tipo de SEQUENCE integrado -> por ende puede ser INDEXADO y REBANADO
       > soporta OPERACION de CONCATENACION:
           >>> cuadrados = [1, 4, 10]
           >>> cuadrados + [16, 25]
           [1,4109,16,25]
           
       > a diferencia de las STRINGS, que son INMUTABLE, las LISTAS son MUTABLE
       >>> cuadrados[2] = 9
       [1,4,9,16,25]
       
       >>> cuadrados.append(36)
       >>> cuadrados.append(7 ** 2)
       >>> cuadrados
       [1,4,9,16,25,36,49]
       
       >>> cuadrados[2:5] = ['nueve','dieciseis','veinticinco']
       >>> cuadrados
       [1,4,'nueve','dieciseis','veinticinco',36,49]
       
       >>> cuadrados[2:5] = []
       >>> cuadrados
       [1,3,36,49]
       
       >>> cuadrados[:] = []
       >>> cuadrados
       []
       
       >>> letras = ['a','b','c']
       >>> len(letras)
       3
       
       > es posible anidar listas que contengan listas
       > y cuando se ponen dos pares de corchetes, se elije el elemento que dentro
       >>> l = [letras, 2]
       >>> l[0][1]
       'b'
       
       >>> list[:-n] # le quita n desde el final  
       >>> list[::-1] # lo invierte
       >>> list[::2] # deja el 0 y el 2do, y asi
       >>> list[::3] # deja el 0 y del 3ero, el 6to, y asi ... al infinito
       >>> list[::-2] # si empieza en cero y termina en impar, el cero no esta. Invierte y quita.
       >>> list[::-3] # multiplos de 3, el 0 va a estar al final
       
4) SENTENCIAS: sentencias de control de flujo y...        ¿OTRAS?
    
        A) Sentencia while
        >>> a, b = 0, 1
        >>> while b < 10:
            print(b)
            a, b = b, a + b
        1 > 1 > 2 > 3 > 5 > 8
        > los operadores de comparación se escriben igual que en C
        > >, <, == (igual a), <= (menor o igual que), >= (mayor o igual que)
        > != (distinto a)
        
        PAG 23 -> completar y extraaer subrayados
        
        B) Sentencia if
        >>> x = int(input("Ingresa un numero entero: "))
        3
        >>>  if x < 0:
        ...      X = 0
        ...      print("Negativo cambiado a cero")
        ...  elif x == 0:
        ...      print('Cero')
        ...  else x < 0:
        ...       print('Entero')
        ... 
        Entero
       
        PAG 24 completar 
        
        C) Sentencia for
        >>> for p in palabras:
                print(p, len(p))
                
                COMPLETAR
    
    A) Sentencia if
    B) Sentencia for
    C) Funcion range()
        
    D) Sentencia BREAK, CONTINUE
        
"""
""" 
ME COSTO BOCHA ENTENDER. COMO EN EL 4, POR EJEMPLO, 4 % 3 NO ES == 0
AHI NO SE IMPRIME Y VA AL 'SIGUIENTE FOR', CUANDO SUCEDE EL break ENTONCES
QUEDA IMPRIMIDO LO QUE SE HABIA IMPRIMIDO, PERO SI PASA DE LARGO Y NO SUCEDE
EL BREAK -> SE IMPRIME EL else  
"""

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0: 
            print(n, 'es igual a', x, '*', n/x)
            break
        
    else:
        print(n, 'es un numero primo')
        
"""        
    E) Sentencia PASS
""" 

print('\n E) SENTENCIA PASS'
      '\nNo la termine de entender')

"""
    F) Definiendo funciones
        
        > Esta es la parte que más ejercite creo, vamos a probar:
"""
def acordeC():
    print('E | | | | '
          '\nB |o| | | '
          '\nG | | | | '
          '\nD | |o| |'
          '\nA | | |o|'
          '\nE | | | | ')
acordeC()


"""     
5) FUNCIONES: ¿qué son?¿qué hacen? -> dibujarlas
        print() es una función
N) Argumentos
3) Parametros
4) Valores
    
5) Variables regulares_'
    > MODO INTERACTIVO (Terminal): la última EXPRESION IMPRESA es ASIGNADA a la VARIABLE '_'
    
6) Docstrings (cadenas de documentos: " x 3 )
7) Modulos
8) Excepciones

###
A ACOMODAR EN ALGUN LADO:
def
int("0")
str(0
###

# En una lista


# cosas que no se porque se me pasaron
iter('abcdef')
print("next(it), end = ") # o algo así
filter(x,y)
variable[::10] #con x2 dos puntos, tambien vi con x1 dos puntos

#Dentro de 'IMPORT math'
abs(-numero) # lo vuelve positivo
math.factorial(4.0) #al 1 es 1, al 0 es 1, al 2 es 2, y a partir del tres se multiplica por el resultado del numero anterior
"""
