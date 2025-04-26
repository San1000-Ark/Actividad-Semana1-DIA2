#Crea una lista con algunos nombres (por ejemplo: "Ana", "Luis", "Sofía").
#Pide al usuario su nombre.
#Usa if para decir si está en la lista de invitados o no.

NameList=["Ana","Luis","Sofia"]

InputUser=input("Ingresa tu nombre: ")

if InputUser in NameList:
    print("Esta en la lista de invitados...")
else:
    print("No esta en la lista de invitados...")