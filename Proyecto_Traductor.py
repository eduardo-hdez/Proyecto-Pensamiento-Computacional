"""
En esta función, lo que hago es almacenar los datos del código morse y las
letras en el alfabeto en español en listas para luego ser usadas más adelante
"""

def datos():
    codigo_morse_letras = [
        [".-", "A"], ["-...", "B"], ["-.-.", "C"], ["-..", "D"], [".", "E"],
        ["..-.", "F"], ["--.", "G"], ["....", "H"], ["..", "I"], [".---", "J"],
        ["-.-", "K"], [".-..", "L"], ["--", "M"], ["-.", "N"], ["---", "O"],
        [".--.", "P"], ["--.-", "Q"], [".-.", "R"], ["...", "S"], ["-", "T"],
        ["..-", "U"], ["...-", "V"], [".--", "W"], ["-..-", "X"], ["-.--", "Y"],
        ["--..", "Z"]]
    
    codigo_morse_especiales = [
        [".----", "1"], ["..---", "2"], ["...--", "3"], ["....-", "4"],
        [".....", "5"], ["-....", "6"], ["--...", "7"], ["---..", "8"],
        ["----.", "9"], ["-----", "0"], [".-.-.-", "."], ["--..--", ","],
        ["..--..", "?"], [".----.", "'"], ["-.-.--", "!"], ["-..-.", "/"],
        ["-.--.", "("], ["-.--.-", ")"], [".-...", "&"], ["---...", ":"],
        ["-.-.-.", ";"], ["-...-", "="], [".-.-.", "+"], ["-....-", "-"],
        ["..--.-", "_"], [".-..-.", '"'], ["...-..-", "$"], [".--.-.", "@"]]

    return codigo_morse_letras, codigo_morse_especiales

"""
En estas dos funciones, se hace la traducción de texto a código morse y de 
texto a código morseusando un ciclo "for" y con la ayuda de las funciones 
upper() y strip() para que el texto ingresado por el usuario no limite a 
este a escribir su texto de una manera en la yo le indique. Esto hace que 
el usuario pueda tener más libertad a la hora de escribir su texto y 
traducirlo a código morse y viceversa.
"""

def traduccion_texto(palabra):
    codigo_morse_letras, codigo_morse_especiales = datos()

    texto = ""
    
    for x in palabra.upper():
        if x == " ":
            texto = texto + "/"
        else:
            for morse, letra in codigo_morse_letras:
                if letra == x:
                    texto = texto + morse + " "
                    break
            else:
                for morse, caracter in codigo_morse_especiales:
                    if caracter == x:
                        texto = texto + morse + " "
                        break

    return texto.strip()

def traduccion_morse(texto_morse):
    codigo_morse_letras, codigo_morse_especiales = datos()
    
    palabras = texto_morse.split("/")
    texto = ""
    
    for palabra_morse in palabras:
        letras_morse = palabra_morse.strip().split()
        for letra_morse in letras_morse:
            for morse, letra in codigo_morse_letras:
                if letra_morse == morse:
                    texto = texto + letra
                    break
            else:
                for morse, caracter in codigo_morse_especiales:
                    if caracter == morse:
                        texto = texto + caracter
                        break
        texto = texto + " "
    
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
        print("2) Traductor de Código Morse a Texto")
        print("3) Salir \n")

        opcion = input("Elija una opción del 1 al 3: ")

        if opcion == "1":
            frase = input("Ingrese un texto en español: ")
            morse = traduccion_texto(frase)
            print("La traducción del texto a código Morse es:\n", morse)
        elif opcion == "2":
            morse = input("Ingrese un código Morse: ")
            texto = traduccion_morse(morse)
            print("La traducción de código Morse a texto es:\n", texto)
        elif opcion == "3":
            print("¡Adiós! Gracias por usar este programa.")
            break
        else:
            print("Opción incorrecta. INTENTE DE NUEVO.")

menu()

