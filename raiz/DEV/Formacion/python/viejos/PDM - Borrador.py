#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 00:30:25 2020

@author: hale
"""
# Trabajando la OP 1

	if op =="1":
		print("\nEscribe la nota en minuscula. En caso de que quieras la escala de Re sostenido por ejemplo, tecleá 're#'\n")
        nota = input("Nota: ")
		while nota in n:
			calcularEscala(nota)
			nota = input("\nPrueba con otra nota: ")


# Borrador de 'programa de musica' ; probando usar index
nota = input()
	
	notas["Do, Do#, Re, Re#, Mi, Fa, Fa#, Sol, Sol#, La, La#, Si, Do, Do#, Re, Re#, Mi, Fa, Fa#, Sol, Sol#, La, La#, Si, Do"]
	es = notas.index(nota)
	
	
	
	mayor(notas[x], notas[x + 2], notas[x + 4], notas[x + 5], notas[x + 7], notas[x + 9], notas[x] + 11], notas[[x] + 12],)
	
# Lo que antes se llamaba 'programa de musica' ; creo que es la primer version
    
    print("Hola, bienvenide. Dime tu nombre: ")
nombre = input()	
while True:
	print("Hola " + nombre + " , en este programa podras consultar distinta información sobre música")
	print("Tengo estas opciones para ofrecerte:")
	print("1) Escalas")
	print("2) Acordes")
	print("3) Tonos")
	op = input()		
	if op == "1":
		print("Escribe en minuscula la nota")
		nota = input()
		if nota == "do":
			print("Do M: Do, Re, Mi, Fa, Sol, La, Si, Do")
			print("Do m: Do, Re, Re#, Fa, Sol, Sol#, La#, Si#")
		if nota == "re":
			print("Re M:")
			print("Re m:")
		if nota == "mi":
			print("Mi M:")
			print("Mi m:")
		if nota == "fa":
			print("Fa M:")
			print("Fa m:")
	continue