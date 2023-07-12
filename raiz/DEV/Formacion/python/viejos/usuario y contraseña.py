def usuario_contraseña():
	usuario = input("Hola, bienvenide!\nInventa un usuario: ")
	n = ["do", "do#", "re", "re#", "mi", "fa", "fa#", "sol", "sol#", "la", "la#", "si", "Do", "Do#", "Re", "Re#", "Mi", "Fa", "Fa#", "Sol", "Sol#", "La", "La#", "Si", "Do"]
	print("\nHola " + usuario + ", en este programa podras consultar cierta información sobre música. Pero para eso debes ingresar una contraseña que tenga 5 números")
	pas = input("Contraseña: ")
	while True:  
		if len(pas) == 5:
			print("\nMuy bien, ahora ingresa tu usuario y tu contraseña...")
			break
		elif len(pas) < 5:
			print("Muy corta, vuelve a intentarlo")
			pas = input("Contraseña: ")
			continue
	while True:
		usuario2 = input("Usuario: ")
		if usuario == usuario2:
			pas2 = input("Contraseña: ")
		else:
			print("Usuario incorrecto")
			continue
		if pas2 == pas:
			input("Has ingresado con éxito, presiona ENTER")
			break
		else:
			print("Error, vuelve a intentarlo")
			continue
			
usuario_contraseña()