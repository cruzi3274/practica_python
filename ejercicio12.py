ventas = []

while True:
    producto = input("Producto (o 'fin' para terminar): ")
    if producto == "fin":
        break
    precio = float(input("Precio de venta: $"))
    costo = float(input("Lo que te costó: $"))
    ventas.append({"producto": producto, "ganancia": precio - costo})

total = sum(v["ganancia"] for v in ventas)
print(f"\nVentas registradas: {len(ventas)}")
print(f"Ganancia total: ${total}")