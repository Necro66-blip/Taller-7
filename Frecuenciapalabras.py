parrafo = "python es versatil y python es legible y practico"


palabras = parrafo.split()


frecuencia = {}
for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1


print("--- Frecuencia de palabras ---")
for palabra, conteo in frecuencia.items():
    print(f"Palabra: {palabra:<10} | Recuento: {conteo}")