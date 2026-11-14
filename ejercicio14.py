tipo = int(input("Ingrese el tipo de viaje: "))
kilo = int(input("Ingrese cantidad de kilo a transportar: "))
costoTotal = 0


if(tipo == 1):
    costoTotal = 1500
    if(kilo > 20):
        costoTotal = costoTotal + (kilo - 20) * 800
elif(tipo == 2):
    costoTotal = 2000

    if(kilo > 20):
        costoTotal =  costoTotal + (kilo / 5) * 800

print("EL costo total es:", costoTotal)
