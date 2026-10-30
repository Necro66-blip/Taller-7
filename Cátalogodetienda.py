cátalogo = {
    "P01": {"nombre": "Cuaderno argollado", "precio": 6500, "stock": 20},
    "P02": {"nombre": "Caja de boligrafos", "precio": 18000, "stock": 12},
    "P03": {"nombre": "Paquete de papel higienico", "precio": 15000, "stock": 8}
}

while True:
    print("\n--- Cátalogo de tienda ---")
    print("1. Buscar producto")
    print("2. Ingrese la existencias (Solo si desea aumentar el stock)")
    print("3. Registrar nuevo producto")
    print("4. Calcular valor total del inventario")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
       
        codigo = input("Ingrese el código del producto (ej. P01): ")
        producto = catalogo.get(codigo)
        if producto:
            print(f"\nDetalles del producto {codigo}:")
            print(f" - Nombre: {producto['nombre']}")
            print(f" - Precio unitario: ${producto['precio']:,.2f}")
            print(f" - Stock disponible: {producto['stock']}")
        else:
            print(f" Advertencia: El código '{codigo}' no existe en el catálogo.")
            
    elif opcion == "2":
        
        codigo = input("Ingrese el código del producto a actualizar: ")
        if codigo in catalogo:
            try:
                cantidad_extra = int(input("Ingrese la cantidad a agregar al stock: "))
                if cantidad_extra > 0:
                    catalogo[codigo]["stock"] += cantidad_extra
                    print(f" Stock actualizado. Nuevo stock de {catalogo[codigo]['nombre']}: {catalogo[codigo]['stock']}")
                else:
                    print("La cantidad debe ser mayor a cero.")
            except ValueError:
                print("Error: Ingrese un valor numérico válido.")
        else:
            print(" Advertencia: El código ingresado no existe.")
            
    elif opcion == "3":
       
        codigo = input("Ingrese el código para el nuevo producto (ej. P04): ")
        if codigo in catalogo:
            confirmar = input(f"El código '{codigo}' ya existe ({catalogo[codigo]['nombre']}). Desea modificarlo? (s/n): ")
            if confirmar.lower() != 's':
                print("Operación cancelada.")
                continue
                
        nombre = input("Ingrese el nombre del producto: ")
        try:
            precio = float(input("Ingrese el precio unitario: "))
            stock = int(input("Ingrese la cantidad inicial en bodega: "))
            
            catalogo[codigo] = {
                "nombre": nombre,
                "precio": precio,
                "stock": stock
            }
            print(f"¡Producto '{nombre}' registrado con éxito!")
        except ValueError:
            print("Error en los datos numéricos. Por favor intentelo de nuevo.")
            
    elif opcion == "4":
        
        valor_total = 0
        print("\n--- Valorizacion del inventario ---")
        for codigo, datos in catalogo.items():
            subtotal = datos["precio"] * datos["stock"]
            valor_total += subtotal
            print(f"[{codigo}] {datos['nombre']}:Stock {datos['stock']} x ${datos['precio']:,.2f} = ${subtotal:,.2f}")
        print(f"\n El inventario está valorizado en: {valor_total:,.2f}")
        
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Por favor intentelo de nuevo.")
