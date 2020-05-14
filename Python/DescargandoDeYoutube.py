
import pafy

def descargarVideo(enlaceYoutube):

		video = pafy.new(enlaceYoutube)
		archivoVideo = video.getbest(preftype="mp4")
		archivoVideo.download()


def descargarAudio(enlaceYoutube):

	audio = pafy.new(enlaceYoutube)
	archivoAudio = audio.getbestaudio()
	archivoAudio.download()


def menu():

	opcion = 0

	while opcion <= 3 or opcion != 3:
		
		banner = """ 
			________           _____.___.              __       ___.           
			\______ \          \__  |   | ____  __ ___/  |_ __ _\_ |__   ____  
			 |    |  \   ______ /   |   |/  _ \|  |  \   __\  |  \ __ \_/ __ \ 
			 |    `   \ /_____/ \____   (  <_> )  |  /|  | |  |  / \_\ \  ___/ 
			/_______  /         / ______|\____/|____/ |__| |____/|___  /\___  >
			        \/          \/                                   \/     \/ 

		"""

		print(banner)
		print()
		print("****************************************************************")
		print("* 															  *")
		print("*	1.-Descargar a video                                      *")
		print("*	2.-Descargar a Audio                                      *")
		print("* 	3.-Salir         										  *")
		print("*															  *")
		print("****************************************************************")
		opcion = int(input(">> Escoge una opcion : "))

		if opcion == 1:

			urlYoutube= input(">>Ingrese la url del video de youtube : ")
			descargarVideo()

		elif opcion  == 2:

			urlYoutube= input(">>Ingrese la url del video de youtube : ")
			descargarAudio()

		elif opcion == 3:

			print(" A salido del sistema ")
			break

		else:

			print("------------ Debe ingresar una opcion valida -------------")





def main():
	menu()


main()
