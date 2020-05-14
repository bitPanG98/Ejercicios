#!usr/bin/env python
# -*- coding: utf-8 -*-

def show_banner():
   
   path_file = "configuracion/banner.txt"
   
   file = open(path_file, "r")
   banner =   file.read()
   file.close()
   print(banner)
   
show_banner()















   