#Pide tres números al usuario. Usa condicionales (if) para decir cuál es el más pequeño.

numero1=int(input("Ingresa el primer numero: "))
numero2=int(input("Ingresa el segundo numero: "))
numero3=int(input("Ingresa el tercer numero: "))

print("Los numeros ingresados son: ", numero1, numero2, numero3)

if numero1!=numero2 and numero1!=numero3 and numero2!=numero3:
    if numero1<numero2:
        if numero1<numero3:
            print("El numero menor es numero1: ",numero1)
        else:
            print("El numero menor es numero3: ",numero3)
    else:
        if numero2<numero3:
            print("El numero menor es numero2: ",numero2)
        else:
            print("El numero menor es numero3: ",numero3)

else:
    print("Ingresa 3 numeros diferentes")