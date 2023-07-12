
"""
 PYTHON

            (TUTORIAL DALTO)

            1. Lenguaje de propósito general
            2. lenguaje de alto nivel
            3. fácil de aprender (curva de aprendizaje más sensilla de todas - rápido aprendizaje)
            4. tipado dinámico (la variable se adapta según el tipo de dato que le demos)
            5. Lenguaje orientado a objetos
            6. Lenguaje interpretado (a diferencia del compilado {parecido a renderizar un video}, este ejecuta línea por línea) → interpreta y ejecuta a la vez.

            PORQUE USAR PYTHON
            Es multiparadigma (puede usarse en Mac, Windows, Linux);
            
            <!-- INSTALAR la extension -->
            <!-- Prettier ; python ident -->
            * Instalamos las extensiones : PRETTIER ; PYTHON IDENT.
            * si escribimos "clear", se limpia la consola

        #################
        I. CONCEPTOS BASICOS
        #################

        (A.1) Hay tipos de datos; (simples = 4) 
            1. STRING [str] (texto, cadena de texto) -> 
            2. NUMEROS (int: enteros)
            3. NUMEROS FLOAT (flotantes, con decimales)
            4. Booleano (True / False) 

        (B) Variables (espacios que se almacenan en la memoria de nuestro programa)
            * las variables se DECLARAN, y de DEFINEN.
            * son modificables (se pueden REDEFINIR)
            * Concatenación (cuando unimos)
            * F-string (todo lo convierte a texto, si hay alojado en la variable algo que no sea STR) → disponibles desde PYTHON 3.6
            * si queremos eliminar una variable, utilizamos el OPERADOR 'del'
            * hay otros operadores de PERTENENCIA y de IDENTIDAD

        (A.2) Datos compuestos : datos que alojan Datos
            * datos que tienen adentro datos simples u otros datos compuestos    
            1. listas "LIST" 
            * contamos desde el "0"
            <!-- * ARRAY (arreglo), es otro tipo de matríz -->
            2. TUPLA (usamos en vez de corchetes, paréntesis) → la diferencia es que no se puede modificar.
            3. SET (conjunto)
                * para crearlo usamos '{}'
                * elementos desordenados; no tienen un orden fijo; pueden cambiar/intercambiarse
                * pdemos reconstruír, pero no podemos cambiar cada elemento en particular
                * no podemos acceder al conjunto por el [indice].
                * no me permite repetir valores, no puede haber duplicados
                * si se puede ITERAR
                * para acceder, se puede utilizar un BUCLE
            4. diccionario (dict)
            
        (C) Operadores
            1. aritméticos (matemáticos)



# tipos de datos
    # Para texto, '' (str) ; "string" = cadena de texto

"String"
'Solo una línea'
"""


""" 
Si queremos hacer múltiples lineas
"""

'''También 
multiples lineas'''

#(B) VARIABLES

# concatenar con +
nombre = "Esteban"
nombre += " 'Tevo' Etter"

# Para introducir variables en un string ; f-strings ; no hace falta que la variable sea un 'str'.
bienvenida = f"Hola {nombre} ¿Cómo estas?"

# para eliminar una variable
del bienvenida

# concatenar con f-strings
nombre = "Gato"
bienvenide = f"Hola {nombre} .. ¿Qué tul?"

print("hola mundo")

# operaciones de pertenencia (in / not in)
print("ola" in bienvenide)
print("Pedro" not in bienvenide)

# y de identidad

# camelCase → para definir variables
nombreCompletoDelAsunto = "Estoy usando camelCase para definir variables"

# snake_case → recomendada por PYTHON
nombre_completo_de_la_serpiente = "usando snake_case, recomendada por python"



######### (A.2) DATOS COMPUESTOS

# 1. list = [,]
lista = ["hola",5,7,"como sabes que soy yo?","José"]
print(lista[1])

# 2. tupla
tupla = ("no, se puede, modificar", 5, "6")

# 3. creando un conjunto (SET)
conjunto = {"no", 5}

# 4. diccionario (dict)
diccionario = {
    'nombre' : "Alejandro Ruiz", # key : value,
    'edad' : 31,
    'profesion' : "Actor"
}

print(diccionario['nombre'])

########### OPERADORES ARITMÉTICOS
'''
suma (+)
resta (-)
multi (*)
divi (/) # devuelve FLOAT
potenciacion/exponente (**)
divi baja (//) → redondea hacia abajo
módulo o resto (%) → devuelve lo que sobra de la división
'''

tipo_de_dato = type(division_baja) # type(dato) nos devuelve qué tipo de dato es
 
print(tipo_de_dato)

##### operadores de comparación (son seis -6-) DEVUELVEN T/F

"""
==  → es igual que 
!=  → es distinto a
<   → es menor que 
<=  → menor o igual
>   → mayor que
>=  → mayor o igual
"""

# comparar usuarios
usuario_database = "Alejandro Ruiz"
usuario_escrito = "Alejandro"

'''
def inPass {
    if input(pasword) == 
}
'''







