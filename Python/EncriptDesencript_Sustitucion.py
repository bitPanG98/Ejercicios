
letrasAlfabeto = [
                                 "a" , "b" , "c" , "d"  , "e" , "f" ,  "g" , "h" , "i" , "j" , "k" , "l" , "m" ,
                                 "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z" , " ",
                                 "1" ,  "2" , "3" , "4" , "5", "6" , "7" ,  "8" , "9" , "0"                                 
                             ]

letrasSustituir = [
                                "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" , "x" , "y" , "z" ,
                                 "a" , "b" , "c" , "d"  , "e" , "f" ,  "g" , "h" , "i" , "j" , "k" , "l" , "m" , "*",
                                "9" ,  "1"  , "8" , "2" , "7", "3" , "6" ,  "4" , "5" , "0"
                              ]

textoEncriptado = ""
textoDesencriptado = ""

indicesAlfabeto = []
indicesLetrasSustituir = []

texto = input("\n>> Ingrese texto a encriptar : ")

#--------------------------------ENCRIPTAR EL TEXO INGRESADO ------------------------------------------

for caracter in texto:

    if caracter in letrasAlfabeto:

        posicionObtenida = letrasAlfabeto.index(caracter)
        indicesAlfabeto.append(posicionObtenida)
        
for posicion in indicesAlfabeto:

    textoEncriptado += letrasSustituir[posicion]

print("\n>> El texto encriptado es :  ",textoEncriptado)

#------------------------------------DESENCRIPTAR EL TEXTO CODIFICADO--------------------------------

textoDesencriptar = input("\n>>Ingrese texto a desnecriptar  : ")

for caracter in textoDesencriptar:
    
    posicionObtenida =  letrasSustituir.index(caracter)
    indicesLetrasSustituir.append(posicionObtenida)


for posicion in indicesLetrasSustituir:
    textoDesencriptado +=  letrasAlfabeto[posicion]

print("\n>>El texto desencriptado :  " , textoDesencriptado)
