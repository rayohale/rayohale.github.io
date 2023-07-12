# 't' de traste
t0 = "#|   |   |   |   |"
t1 = "#| o |   |   |   |"
t2 = "#|   | o |   |   |"
t3="#|   |   | o |   |"
t4="#|   |   |   | o |"
	
# 'c' de cuerda
def acorde(c6, c5, c4, c3, c2, c1):
	print("E " + c6)
	print("A " + c5)
	print("D " + c4)
	print("G " + c3)
	print("B " + c2)
	print("E " + c1 +"\n")



def acorde_Em():
	print("E " + t0)
	print("A " + t2)
	print("D " + t2)
	print("G " + t0)
	print("B " + t0)
	print("E " + t0 + "\n")
def acorde_E():
	acorde(t0,t2,t2,t1,t0,t0)	
def acorde_A():
	acorde(t0,t0,t2,t2,t2,t0)
def acorde_Am():
	acorde(t0,t0,t2,t2,t1,t0)
def acorde_G():
	acorde(t3,t2,t0,t0,t3,t3)
def acorde_Gm():
	acorde(t3,t2,t0,t0,t0,t3)

