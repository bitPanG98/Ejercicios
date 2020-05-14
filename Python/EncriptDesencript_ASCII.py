#----Programa que permite ENCRIPTAR Y DESENCRIPTAR una cadena de texto----

#---> ENCRIPTAR : sumandole una cantidad a su codigo ASCII
#---> DESENCRIPTAR: restandole una cantidad a su codigo ASCII 



def encriptarTexto(texto):

    miTextoEncriptado = ""
    codigosASCII = []


    for caracter in texto:

        codigosASCII.append( ord(caracter) + 5)

    for codigo in codigosASCII:
      
        miTextoEncriptado += chr(codigo)

    print("\nTexto encriptado es  : ", miTextoEncriptado)



def desencriptarTexto(miTextoEncriptado):

    miTextoDesencriptado = ""
    
    codigosASCII = []

    for caracter in miTextoEncriptado:

        codigosASCII.append( ord(caracter) - 5 )

    for codigo in codigosASCII:

        miTextoDesencriptado += chr(codigo)

    print("\nTexto Desencriptado es  : ", miTextoDesencriptado)


# FUNCION DEL MENU
def menu():

    opcion = 0

    while opcion <= 3 or opcion != 3:

        try:

            print()
            print("  ----------------------------------------------------------------   ")
            print("         Programa de encriptado y desencriptado          ")
            print("  ----------------------------------------------------------------   ")
            print("                                                                                          ")
            print("     1.-Encriptar                                                                 ")
            print("     2.-Desencriptar                                                           ")
            print("     3.-Salir                                                                          ")
            print("                                                                                           ")
            print("  -----------------------------------------------------------------  ")

            opcion = int(input("Digite opcion : "))
        
            if opcion == 1:
        
                texto = input("\n>> Digite texto a encriptar : ")
                encriptarTexto(texto)

            elif opcion == 2:

                miTextoEncriptado = input("\n>> Digite texto a Desencriptar : ")
                desencriptarTexto(miTextoEncriptado)

            elif opcion == 3:

                print("\n------ A finalizado el programa ------ ")
                break  

            else:

                print("\n--- Opcion elegida no valida ---")

        except ValueError:
            print("\n--- Opcion elegida no valiida ---")

#Llamamos a la funcion menu para ejecutar el programa
menu()
