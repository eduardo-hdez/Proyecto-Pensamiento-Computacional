#Funciones

def txt_a_morse():
    txt = str(input("Introduce una letra para ser traducido a"
                    "\ncódigo morse: ")).lower()
    
    if txt == "a":
        return ".-"
    elif txt == "b":
        return "-..."
    elif txt == "c":
        return "-.-."
    elif txt == "d":
        return "-.."
    elif txt == "e":
        return "."
    elif txt == "f":
        return "..-."
    elif txt == "g":
        return "--."
    elif txt == "h":
        return "...."
    elif txt == "i":
        return ".."
    elif txt == "j":
        return ".---"
    elif txt == "k":
        return "-.-"
    elif txt == "l":
        return ".-.."
    elif txt == "m":
        return "--"
    elif txt == "n":
        return "-."
    elif txt == "ñ":
        return "--.--"
    elif txt == "o":
        return "---"
    elif txt == "p":
        return ".--."
    elif txt == "q":
        return "--.-"
    elif txt == "r":
        return "-.-"
    elif txt == "s":
        return "..."
    elif txt == "t":
        return "-"
    elif txt == "u":
        return "..-"
    elif txt == "v":
        return "...-"
    elif txt == "w":
        return ".--"
    elif txt == "x":
        return "-..-"
    elif txt == "y":
        return "-.--"
    elif txt == "z":
        return "--.."
    else:
        return "El texto no es válido. INTENTE DE NUEVO."

    
def morse_a_txt():
    txt2 = str(input("Introduce un código morse para ser"
                     "\ntraducido a texto: ")).lower()
    
    if txt2 == ".-":
        return "a"
    elif txt2 == "-...":
        return "b"
    elif txt2 == "-.-.":
        return "c"
    elif txt2 == "-..":
        return "d"
    elif txt2 == ".":
        return "e"
    elif txt2 == "..-.":
        return "f"
    elif txt2 == "--.":
        return "g"
    elif txt2 == "....":
        return "h"
    elif txt2 == "..":
        return "i"
    elif txt2 == ".---":
        return "j"
    elif txt2 == "-.-":
        return "k"
    elif txt2 == ".-..":
        return "l"
    elif txt2 == "--":
        return "m"
    elif txt2 == "-.":
        return "n"
    elif txt2 == "--.--":
        return "ñ"
    elif txt2 == "---":
        return "o"
    elif txt2 == ".--.":
        return "p"
    elif txt2 == "--.-":
        return "q"
    elif txt2 == "-.-":
        return "r"
    elif txt2 == "...":
        return "s"
    elif txt2 == "-":
        return "t"
    elif txt2 == "..-":
        return "u"
    elif txt2 == "...-":
        return "v"
    elif txt2 == ".--":
        return "w"
    elif txt2 == "-..-":
        return "x"
    elif txt2 == "-.--":
        return "y"
    elif txt2 == "--..":
        return "z"
    else:
        return "El código morse no es válido. INTENTE DE NUEVO."

"""
-------------------------------------------------------------------------------
"""


#Loops

while True:
    opcion = input("Introduzca el número de opción que desee usar:"
    "\n1. Texto a código Morse"
    "\n2. Código Morse a texto"
    "\n3. Salir del programa"
    "\n")
    
    if opcion == "1":
        print("El código morse de este texto es:", txt_a_morse())

    elif opcion == "2":
        print("El texto de este código morse es:", morse_a_txt())

    elif opcion == "3":
        print("¡Adiós!")
        break
    
    else:
        print("Esta opción no es válida. INTENTE DE NUEVO.")
        opcion = (input("Introduzca el número de opción que desee usar:"
        "\n1. Texto a código Morse"
        "\n2. Código Morse a texto"
        "\n3. Salir del programa"
        "\n"))


"""
morse_txt = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
              '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
              '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
              '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
              '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
              '--..': 'Z'}
"""



    
