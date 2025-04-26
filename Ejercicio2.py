#Verificar si un número está en una lista Crea una lista con 5 números.Pide un número al usuario y verifica si está en la lista usando in
ListaNumeros=[2,8,10,15,35]

print("Los numeros de la lista son: ",ListaNumeros)

Numero=int(input("Ingresa un Numero cualquiera: "))

if Numero in ListaNumeros:
    print(f"El numero {Numero} esta en la lista")
else:
    print(f"El numero no esta en la lista")