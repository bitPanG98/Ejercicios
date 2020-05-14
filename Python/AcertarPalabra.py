
import random


def ayuda():

	primerCaracter = palabraAcertar[0]
	ultimoCaracter = palabraAcertar[ len(palabraAcertar) - 1 ]

	if contador == 1:
		asteriscos = "*" * ( len(palabraAcertar ) - 1 )
		print("  ", primerCaracter, asteriscos)

	elif contador == 2:
		asteriscos = "*" * ( len(palabraAcertar ) - 2 )
		print("  ", primerCaracter, asteriscos, ultimoCaracter)



acerto = False

contador = 0

palabras= [ "William" , 
         	        "Teodora" ,
         	        "Edson", 
                    "Irvin",
         	        "Edinson",
         	        "Angy" ]

palabraAcertar = random.choice(palabras)

logo = """
------------------------------------------------------------

           	Juego - ACERTAR   PALABRA
           	  	 v. 1.0.0

 -----------------------------------------------------------
"""
print(logo)


while acerto==False:

	palabraIngresada = input("\n>>Digite palabra : ")

	if palabraIngresada == palabraAcertar:

		acerto = True
		print("\n------> Felicitaciones <------ \nA acertado la palabra ")
	
	else:

		acerto = False
		print("\n---->Opps, Siga intentandolo <----")

		contador += 1

		ayuda()

		if contador == 3:

			print(f"\n------> Perdio <------\nA finalizado el programa ,  realizo todos los {contador}  intentos \
			\nLa palabra fue ==> ", palabraAcertar)

			break

