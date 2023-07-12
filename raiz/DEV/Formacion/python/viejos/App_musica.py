#!usr/bin/python
def noDisponible():
	print("Este entorno aún no está construído.\nDisculpe las molestias, estamos trabajando para usted.")
def escalaMayor(x):
	print("Escala M: ", n[x], n[x + 2], n[x + 4], n[x + 5], n[x + 7], n[x + 9], n[x + 11], n[x + 12])
def escalaMenor(x):
	print("Escala m: ", n[x], n[x + 2], n[x + 3], n[x + 5], n[x + 7], n[x + 8], n[x + 10], n[x + 12])
def calcularEscala(nota):
	x =n.index(nota)
	escalaMayor(x)
	escalaMenor(x)
# 't' de traste
t0 = "#|   |   |   |   |"
t1 = "#| o |   |   |   |"
t2 = "#|   | o |   |   |"
t3 = "#|   |   | o |   |"
t4 = "#|   |   |   | o |"
	
# 'c' de cuerda
def acorde(c1, c2, c3, c4, c5, c6):
	print("E " + c1)
	print("A " + c2)
	print("D " + c3)
	print("G " + c4)
	print("B " + c5)
	print("E " + c6 +"\n")
# Acorde piloto
def acorde_Em():
	print("MI menor")
	print("E " + t0)
	print("B " + t0)
	print("G " + t0)
	print("D " + t2)
	print("A " + t2)
	print("E " + t0 + "\n")
# Definiendo acordes, usando la func 'acorde'
def acorde_E():
	print("MI Mayor")
	acorde(t0,t0,t1,t2,t2,t0)	
def acorde_A():
	print("LA Mayor")
	acorde(t0,t2,t2,t2,t0,t0)
def acorde_Am():
	print("LA menor")
	acorde(t0,t1,t2,t2,t0,t0)
def acorde_G():
	print("SOL Mayor")
	acorde(t3,t3,t0,t0,t2,t3)
def acorde_Gm():
	print("SOL menor")
	acorde(t3,t0,t0,t0,t2,t3)
def acorde_D():
	print("RE Mayor")
	acorde(t2,t3,t2,t0,t0,t0)
def acorde_Dm():
	print("RE menor")
def acorde_C():
	print("DO Mayor")
def acorde_Cm():
	print("DO menor")
def acorde_F():
	print("FA Mayor")
def acorde_Fm():
	print("FA menor")	

input("Bienvenide a 'BerriosMu'. Presiona ENTER para ir al menú")
while True:	
	print("\nMenú: \n1)Escalas\n2)Acordes\n3)Tonos")
	op = input("Opcion: ")		

	
	if op == "2":
		ac = input("\nIngresa la nota en mayúscula de los acordes que buscas: C, D, E, F, G, A, B: ")
		print(" ")
		final = "acorde_" + ac + "()"
		if ac == "E":
			acorde_E()
			acorde_Em()
		elif ac == "A":
			acorde_A()
			acorde_Am()
		elif ac == "G":
			acorde_G()
			acorde_Gm()
		elif ac == "C":
			acorde_C()
			acorde_Cm()
		elif ac == "D":
			acorde_D()
			acorde_Dm()
		elif ac == "F":
			acorde_F()
			acorde_Fm()
		elif ac == "B":
			acorde_B()
			acorde_Bm()
		
		continue

	if op == "3":
		noDisponible()
		continue
	
	print("Si desea volver al menú principal escriba 'ok', pero si ya ha finalizado escriba 'exit'")
	respuesta = input()
	if respuesta == "ok":
		continue
	elif respuesta == "exit":
		break
	
	
