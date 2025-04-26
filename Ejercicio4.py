#Pide al usuario su edad.
#Si la edad es menor que 0 o mayor que 120, imprime "Edad no válida".
#Si está en el rango correcto, imprime "Edad válida".

edad=int(input("Ingresa tu edad: "))

if edad<=0 or edad>=120:
    print("Ingrese una edad valida")
else:
    print("Edad valida")