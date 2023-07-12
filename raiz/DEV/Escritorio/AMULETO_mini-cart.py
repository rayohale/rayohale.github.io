



def calcularTotal(a,b):
    if a <= 14:
        amuleto_total = 10
    elif a <= 25 and a > 14:
        amuleto_total = 20
    else:
        amuleto_total = 30
    print(amuleto_total+b)
    
calcularTotal(20,7)

