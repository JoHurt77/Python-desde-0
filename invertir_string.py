#EJERCICIO PRÁCTICO 7

string = input("Introduce una frase: ")

string_reversed = ""

for character in string:
    string_reversed = character + string_reversed

print(f"String invertido: {string_reversed}")
