nombre = input("Ingrese el nombre: ")
nota = int(input("Ingrese su nota: "))

if nota == 10:
    print(nombre,"obtuvo un sobresaliente")
elif nota >= 8 and nota <= 9:
    print(nombre,"obtuvo un Distinguido")
elif nota >= 6 and nota <= 7:
    print(nombre,"obtuvo un bueno")
elif nota >= 4 and nota <= 5:
    print(nombre,"obtuvo un Aprobado")
elif nota >= 1 and nota <= 3:
    print(nombre,"obtuvo un Reprobado")
else:
    print("Nota invalido ")
    


