#EJEMPLO DE USO DE REPOSITORIO

print("datos personales")
print("-----------------")
vNom = input("ingrese su nombre: ")
while True:
    try :
     vEdad = int(input("ingrese su edad: "))
     break

    except:
        print("valor no corresponde")

print("-------------------")
print(f"su nombre es: {vNom} ")
print(f"su edad es:   {vEdad} ")

print("Programa finalizado....")