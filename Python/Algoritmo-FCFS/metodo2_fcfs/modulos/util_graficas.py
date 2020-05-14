#!usr/bin/env python3
# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------------------------
# author: SoftPanG
# correo: bitpang98@gmail.com
#-----------------------------------------------------------------------------------------------


#---------------------- funciones ---------------------
def graficar_linea():
   """
   Funcion que permite generar,  una linea numerica
   para graficos.
   """
   
   #variables
   grafica_linea = "|----"*15
   
   return grafica_linea+"|"
   
   
def mostrar_serienumerica():
   """
   Funcion que permite mostrar una sucesion numerica segun un rango
    de valores
    """
    
    #variables
   lista_serie   =   []
   serie_numerica =  ""
   
   #creamos los valores  segun un rango y los almacenamos en una lista
   for num in range(0,16):
      lista_serie.append(num)

   #recorremos los valores de nuestra lista
   for num in lista_serie:
      #verificamos cuantos espacios dejaremos entre cada numero, segun
      #si es unidad, decena o centena.
      if num < 10:
         serie_numerica += str(num)+"    "
 
      else:
          serie_numerica += str(num)+"   "
   
   return serie_numerica


def show_grafica(lista_rafagascpu):
   """
   Funcion que permite graficar barras, recibiendo una lista con los valores
   a graficar.
   """
   
   #variables
   ancho_space = 5
   lista_datosgraficar = []
   color = ""
   posicion=0
   
   colores =  [
                        "\033[41m" , "\033[42m" , "\033[43m" , "\033[44m" ,
                        "\033[45m" , "\033[46m" , "\033[47m"
                      ]
   
   #recorremos los valores de la lista
   for rafaga in lista_rafagascpu:
      
      posicion+=1
      
      color = colores[posicion-1]
      lista_datosgraficar.append((color+str(" "*int(rafaga*ancho_space))))
   
   graficar_barras = "".join([str(dato) for dato in lista_datosgraficar])
   
   print(graficar_barras)
   print("\033[40m"+graficar_linea())
   print(mostrar_serienumerica())











