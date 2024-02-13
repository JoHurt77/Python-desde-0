#EJERCICIO PRÁCTICO 6
frase = input("Introduce una frase: ")
eliminarPalabra = input("Qué letra deseas eliminar?: ")
fraseFinal = ""
#find devuelve un valor
indice = frase.find(eliminarPalabra)
fraseFinal = frase[0:indice] + frase[indice + len(eliminarPalabra) + 1 :]
print(f"Cadena resultante: {fraseFinal}")
