
contraseña = input(">>Ingrese contraseña :  ")

longitud = len(contraseña)

if  longitud < 8:
	
	print("\nLa contraseña debe ser mayor de 8 caracteres")

else:

	print("\nLa contraseña es correcta")