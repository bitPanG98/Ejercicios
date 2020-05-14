#!usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

def show_banner():
   
   #path_file = os.path.dirname(os.path.abspath(__file__))
   #h = os.getcwd()
   #j = os.pardir
   path_archivo = "modulos/banner.txt"
   
   if os.path.isfile(path_archivo):
      
      archivo = open(path_archivo, "r")
      banner = archivo.read()
      archivo.close()
      print(banner)
   
   else:
      print("no existe")
   

   
show_banner()


#Funcion para verificar, si un archivo exxiste o no.
def check_file(file):
   
   existe = False
   
   if os.path.isfile(file):
      existe =   True
   else:
      existe = False

   return existe
   



















