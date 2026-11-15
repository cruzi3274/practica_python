sueldoBasico = 4500
plusAntiguedad = 0.02
Hora_trabajado = int(input("Ingrese cantidad de horas trabajadas: "))
antiguedad = int(input("Ingrese el años de antiguedad: "))
sueldoNeto = sueldoBasico * Hora_trabajado
plus = sueldoNeto * (0.02 * antiguedad)
sueldoNeto = sueldoNeto + plus

print("El sueldo neto es: ", round(sueldoNeto))  
