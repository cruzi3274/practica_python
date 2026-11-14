import random

# ---------- Configuración de niveles ----------
NIVELES = {
    "1": {"nombre": "Fácil", "maximo": 10, "intentos": 5},
    "2": {"nombre": "Medio", "maximo": 50, "intentos": 7},
    "3": {"nombre": "Difícil", "maximo": 100, "intentos": 7},
}


def elegir_nivel():
    print("Elegí un nivel:")
    for clave, datos in NIVELES.items():
        print(f"  {clave}) {datos['nombre']} (número entre 1 y {datos['maximo']}, {datos['intentos']} intentos)")

    while True:
        opcion = input("Nivel: ")
        if opcion in NIVELES:
            return NIVELES[opcion]
        print("Opción inválida, probá con 1, 2 o 3.")


def pedir_numero(maximo):
    while True:
        texto = input("Tu número: ")
        if texto.isdigit() and 1 <= int(texto) <= maximo:
            return int(texto)
        print(f"Escribí un número entero entre 1 y {maximo}.")


def jugar():
    nivel = elegir_nivel()
    secreto = random.randint(1, nivel["maximo"])
    intentos_restantes = nivel["intentos"]

    print(f"\nPensé un número entre 1 y {nivel['maximo']}. Tenés {intentos_restantes} intentos.\n")

    while intentos_restantes > 0:
        intento = pedir_numero(nivel["maximo"])

        if intento == secreto:
            puntos = intentos_restantes * 10
            print(f"¡Ganaste! Era el {secreto}. Puntos: {puntos}")
            return puntos
        elif intento < secreto:
            print("Más alto ⬆️")
        else:
            print("Más bajo ⬇️")

        intentos_restantes -= 1
        print(f"Te quedan {intentos_restantes} intentos.\n")

    print(f"Perdiste 😢 El número era {secreto}.")
    return 0


# ---------- Programa principal ----------
puntaje_total = 0

while True:
    puntaje_total += jugar()
    print(f"\nPuntaje total: {puntaje_total}")
    otra = input("¿Jugar otra vez? (s/n): ").lower()
    if otra != "s":
        break

print("¡Gracias por jugar!")