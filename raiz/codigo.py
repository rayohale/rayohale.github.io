contra = input("Introduzca su contraseña")

import webbrowser

if contra == "elefantes":
    print("contraseña correcta")
    webbrowser.open("http://rayohale.github.io/00_index.html")
else:
    print("contraseña incorrecta")