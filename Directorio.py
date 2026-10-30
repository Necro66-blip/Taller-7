directorio = {
    "Pedro": "3001234567",
    "Maria": "3109876543",
    "Lucía": "3204567890",
    "Mateo": "3156781234",
    "Felipe": "3187654321",
}

nombre_contacto = input("Ingrese el nombre del contacto que desea buscar: ")
telefono = directorio.get(nombre_contacto)

if telefono:
    print(f"Teléfono de {nombre_contacto}: {telefono}")
else:
    print(f"Aviso: El contacto '{nombre_contacto}' no se encuentra registrado en el directorio.")

nuevo_con = input("Si desea actualizar un contacto o añadir uno nuevo, ingrese el nombre: ")
nuevo_tel = input("Ingrese el número de teléfono correspondiente: ")

directorio[nuevo_con] = nuevo_tel  
print(f"Contacto de {nuevo_con} ha sido guardado con éxito.")

print("\n--- Lista de contactos ---")
print(f"{'Nombre':<15} | {'Teléfono'}")
print("-" * 27)

for nombre, tel in directorio.items():
    print(f"{nombre:<15} | {tel}")