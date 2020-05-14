#!usr/bin/env python
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------------------------
# author: SoftPanG
# direccion: bitpang98@gmail.com
#
# descripcion: Algoritmo desarrollado para planificar procesos
#                          utilizando el algoritmo de planificacion FIFO.
#-----------------------------------------------------------------------------------------------

from modulos.util_graficas import show_grafica
from modulos.util import show_banner
import string

#show_banner()

#->Declaracion de variables a utilizar
letras_procesos = string.ascii_uppercase
lista_rafagascpu = []
lista_nombresprocesos = []
rafaga_cpu = 0
cantidad_procesos = 0
proceso = ""

#----------------------------------------------------------------
print("\n")
print("-"*30)
cantidad_procesos = int(input(">>Cantidad de procesos : "))
print("-"*30)

for n in range(cantidad_procesos):

	proceso = letras_procesos[n]
	print("\n>> Proceso ["+proceso+"] : ")
	lista_nombresprocesos.append(proceso)

	rafaga_cpu = int(input("   -> Rafaga de CPU : "))
	lista_rafagascpu.append(rafaga_cpu)

print("-"*30)

#---------------------------------------------------------------
print("\n")
print("-"*35)
print("  Proceso\t\tDuracion")
print("-"*35)
for i in range(len(lista_nombresprocesos)):
	print("Proceso [",lista_nombresprocesos[i],"]\t\t",lista_rafagascpu[i])

#----------------------------------------------------------------

#Graficar diagrama d Gannt
print("\n")
print("="*20," GRAFICA DE GANNT ","="*20)
print("\n")
show_grafica(lista_rafagascpu)
