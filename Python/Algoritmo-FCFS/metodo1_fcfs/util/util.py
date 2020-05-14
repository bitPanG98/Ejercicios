#!usr/bin/env python3
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------------------------
# author: bitPanG98
# direccion: bitpang98@gmail.com
#
# descripcion: Algoritmo desarrollado para planificar procesos
#                          utilizando el algoritmo de planificacion FIFO.
#-----------------------------------------------------------------------------------------------

#modulos
import string


#---------------------- variables a utilizar -----------------------

nombre_proceso =   string.ascii_uppercase



#---------------------- funciones ---------------------
def graficar_linea():
   """
   Funcion que permite graficar una linea grafica
   """
   
   grafica_linea = "|----"*10
   
   return grafica_linea+"|"
   
   
def mostrar_serienumerica():
   """
   Funcion que permite mostrar una sucesion numerica segun un rango
    de valores
    """
    
   lista_serie   =   []
   serie_numerica =  ""
   
   #creamos valores  segun un rango y los almacenamos en una lista
   for num in range(0,11):
      lista_serie.append(num)

   #recorremos los valores de nuestra lista
   for num in lista_serie:
      #verificamos cuantos espacios dejaremos entre cada numero
      if num < 10:
         serie_numerica += str(num)+"    "
 
      else:
          serie_numerica += str(num)+"   "
   
   return serie_numerica


def graficar_barras(lista_rafagascpu):
   """
   Funcion que permite graficar barras, recibiendo una lista con los valores
   a graficar.
   """
   ancho = 5
   elaborar_grafica = ""
   
   colores =  [
                        "\033[41m" , "\033[42m" , "\033[43m" , "\033[44m" ,
                        "\033[45m" , "\033[46m" , "\033[47m"
                      ]

   for rafaga in lista_rafagascpu:
      
      for color in colores:
         elaborar_grafica += color+str(ancho*rafaga)
   
print("\033[40m"+graficar_linea())
print(mostrar_serienumerica())




































