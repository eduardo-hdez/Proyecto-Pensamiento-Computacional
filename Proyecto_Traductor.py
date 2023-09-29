"""
En esta función, lo que hago es almacenar los datos del código morse y las
letras en el alfabeto en español en listas para luego ser usadas más adelante
"""

def datos():
    codigo_morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
                    "..", ".---", "-.-", ".-..", "--", "-.", "--.--" "---",
                    ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--",
                    "-..-", "-.--", "--.."]
    
    letras_espanol = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K",
                      "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U",
                      "V", "W","X", "Y", "Z"]
    
    return codigo_morse, letras_espanol

"""
En esta función, se hace la traducción de texto a código morse usando un ciclo
"for" y con la ayuda de las funciones upper() y strip() para que el texto
ingresado por el usuario no limite a este a escribir su texto de una manera
en la yo le indique. Esto hace que el usuario pueda tener más libertad a la
hora de escribir su texto y traducirlo a código morse.
"""

def traduccion_texto(palabra):
    codigo_morse, letras_espanol = datos()

    texto = ""
    
    for x in palabra.upper():
        if x == " ":
            texto = texto + "/"
        elif x in letras_espanol:
            i = letras_espanol.index(x)
            letras_morse = codigo_morse[i]
            texto = texto + letras_morse + " "

    return texto.strip()

"""
En esta función, lo que hago es la parte del menú del programa donde hago que
la consola imprima las opciones que el usuario pueda ingresar. Luego, si la
opcion es "1", el programa manda al usuario a la funcion traduccion_texto para
que el texto ingresado por el usuario sea traducido a código morse. Si la
opcion es "2", el programa manda al usuario a la funcion traduccion_morse para
que el código morse ingresado por el usuario sea traducido a texto. Si la
opción es "3" el programa saldrá del while loop y se cerrará.
"""

def menu():
    while True:
        print(" \nMenú:")
        print("1) Traductor de Texto a Código Morse")
        print("2) Traductor de Código Morse a Texto (Aún no está listo)")
        print("3) Salir \n")

        opcion = input("Elija una opción del 1 al 3: ")

        if opcion == "1":
            frase = input("Ingrese un texto en español: ")
            morse = traduccion_texto(frase)
            print("La traducción del texto a código morse es:\n", morse)
        elif opcion == "2":
            print("¡Error! Esta opción aún no está disponible.")
        elif opcion == "3":
            print("¡Adiós! Gracias por usar este programa.")
            break
        else:
            print("Opción incorrecta. INTENTE DE NUEVO.")


menu()
