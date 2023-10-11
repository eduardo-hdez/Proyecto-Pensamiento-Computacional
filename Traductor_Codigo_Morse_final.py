"""
Proyecto Libre Python
Traductor de Código Morse.
El programa recibe el texto del usuario y lo traduce a código morse, también
tiene como segunda opción, recibir múltiples código morse y traducirlos
a texto.
"""

"""
======================== Función para almacenar varibales =====================
"""

def datos():
    
    """
    (Uso de funciones y listas anidadas)
    La función se encarga de almancear en 2 listas anidades, los valores de
    cada código morse con su respectiva letra en el alfabeto y también algunos
    carácteres especiales.
    """
    
    codigo_morse_letras = [
        [".-", "A"], ["-...", "B"], ["-.-.", "C"], ["-..", "D"], [".", "E"],
        ["..-.", "F"], ["--.", "G"], ["....", "H"], ["..", "I"], [".---", "J"],
        ["-.-", "K"], [".-..", "L"], ["--", "M"], ["-.", "N"], ["---", "O"],
        [".--.", "P"], ["--.-", "Q"], [".-.", "R"], ["...", "S"], ["-", "T"],
        ["..-", "U"], ["...-", "V"], [".--", "W"], ["-..-", "X"],
        ["-.--", "Y"], ["--..", "Z"]
        ]
    
    codigo_morse_especiales = [
        [".----", "1"], ["..---", "2"], ["...--", "3"], ["....-", "4"],
        [".....", "5"], ["-....", "6"], ["--...", "7"], ["---..", "8"],
        ["----.", "9"], ["-----", "0"], [".-.-.-", "."], ["--..--", ","],
        ["..--..", "?"], [".----.", "'"], ["-.-.--", "!"], ["-..-.", "/"],
        ["-.--.", "("], ["-.--.-", ")"], [".-...", "&"], ["---...", ":"],
        ["-.-.-.", ";"], ["-...-", "="], [".-.-.", "+"], ["-....-", "-"],
        ["..--.-", "_"], [".-..-.", '"'], ["...-..-", "$"], [".--.-.", "@"]
        ]

    return codigo_morse_letras, codigo_morse_especiales

"""
=================== Funciones para traducir texto o código morse ==============
"""

def traduccion_texto(palabra):

    """
    (Uso de funciones, uso de operadores, ciclos, condicionales
    y condicionlaes anidadas)
    Recibe: palabra
    Hace la traducción de texto a código morse mediante usando ciclos que
    revisen la función datos() donde los elementos son guardados y da como
    resultado un texto totalemente traducido sin importar las mayúsculas
    o minúsculas y separando cada código morse con una diagonal "/".
    Devuelve: Código morse traducido del texto
    """
    
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

    """
    (Uso de funciones, uso de operadores, ciclos, ciclos anidados,
    condicionales y condicionlaes anidadas)
    Recibe: texto_morse
    Hace la traducción de código morse a texto mediante usando ciclos para
    revisar la función datos() donde se encuentran almacenados los elementos de
    cada letra con su respectivo código morse, al terminar, da como resultado
    el texto del código morse todo junto sin espacios y no cuenta los
    carácteres espceciales.
    Devuelve: Texto traducido del código morse
    """
     
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
=============================== Menú del programa =============================
"""

def menu():

    """
    (Uso de funciones, ciclos y condicionales)
    Inicializa el menú dando al usuario libertad de ingresar un número
    del 1 al 3, donde cada uno tiene un diferente resultado, el usuario puede
    seguir usando el programa hasta que este ingrese la opcion número 3 donde
    el programa se cierra.
    """
    
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
            morse = input("(ÚNICAMENTE INGRESE LETRAS)"
                          "\n(Separe cada código morse con un espacio)"
                          "\nIngrese un código Morse: ")
            texto = traduccion_morse(morse)
            print("La traducción de código Morse a texto es:\n", texto)
        elif opcion == "3":
            print("¡Adiós! Gracias por usar este programa.")
            break
        else:
            print("Opción incorrecta. INTENTE DE NUEVO.")

menu()
