qst = int(input("""Introduzca el número de opción que desee usar:
1. Texto a código Morse
2. Código Morse a texto
"""))

"""En esta variable he guardado un input que el usario tiene que introducir, le
pide una de las dos opciones que se muestra en el string. He incorporado un
"int" debido a que el input del usuario tiene que ser un número entero.
"""

if qst == 1:
    def txt_a_morse(txt):
        if txt == "a":
            return ".-"
        if txt == "b":
            return "-..."
        if txt == "c":
            return "-.-."
        if txt == "d":
            return "-.."
        if txt == "e":
            return "."
        if txt == "f":
            return "..-."
        if txt == "g":
            return "--."
        if txt == "h":
            return "...."
        if txt == "i":
            return ".."
        if txt == "j":
            return ".---"
        if txt == "k":
            return "-.-"
        if txt == "l":
            return ".-.."
        if txt == "m":
            return "--"
        if txt == "n":
            return "-."
        if txt == "o":
            return "---"
        if txt == "p":
            return ".--."
        if txt == "q":
            return "--.-"
        if txt == "r":
            return "-.-"
        if txt == "s":
            return "..."
        if txt == "t":
            return "-"
        if txt == "u":
            return "..-"
        if txt == "v":
            return "...-"
        if txt == "w":
            return ".--"
        if txt == "x":
            return "-..-"
        if txt == "y":
            return "-.--"
        if txt == "z":
            return "--.."
        if txt == " ":
            return "/"

    texto = str(input("Introduce un texto para ser traducido a código morse: "))
    
    print("El código morse para este texto es:", txt_a_morse(texto))

"""En la primera condicional he decido introducir de igual manera la primera
condicional que en este caso sería la opción número "1". La función que
acompaña la condicional se trata de el trabajo que se hara de texto a código
morse. He guardado dentro de la misma función todas las condicionales que las
letras del abecedario excepto la letra "ñ". Hasta ahora, mis habilidades en
Python solo me permiten llegar al punto en el que se puede traducir una
singular letra a código morse. Al final de la función, la consola imprime
lo que es el resultado del valor obtenido por el usuario a código morse.
"""


elif qst == 2:
    def morse_a_txt(txt2):
        if txt2 == ".-":
            return "a"
        if txt2 == "-...":
            return "b"
        if txt2 == "-.-.":
            return "c"
        if txt2 == "-..":
            return "d"
        if txt2 == ".":
            return "e"
        if txt2 == "..-.":
            return "f"
        if txt2 == "--.":
            return "g"
        if txt2 == "....":
            return "h"
        if txt2 == "..":
            return "i"
        if txt2 == ".---":
            return "j"
        if txt2 == "-.-":
            return "k"
        if txt2 == ".-..":
            return "l"
        if txt2 == "--":
            return "m"
        if txt2 == "-.":
            return "n"
        if txt2 == "---":
            return "o"
        if txt2 == ".--.":
            return "p"
        if txt2 == "--.-":
            return "q"
        if txt2 == "-.-":
            return "r"
        if txt2 == "...":
            return "s"
        if txt2 == "-":
            return "t"
        if txt2 == "..-":
            return "u"
        if txt2 == "...-":
            return "v"
        if txt2 == ".--":
            return "w"
        if txt2 == "-..-":
            return "x"
        if txt2 == "-.--":
            return "y"
        if txt2 == "--..":
            return "z"
        if txt2 == " ":
            return "/"
        
    texto2 = str(input("Introduce un código morse para ser traducido a texto: "))
    
    print("El código morse para este texto es:", morse_a_txt(texto2))

"""Esta siguiente condicional es la segunda opción que el usuario puede elegir,
la condicional es seguida por otra función que en este caso sirve para traducir
de código morse a texto. Al igual que la función de arriba, este solo puede
traducir un simple carácter debido a los conocimientos escasos de Python que
he adquirido durante la materia hasta este punto. Al final de la función la
consola imprime lo que es el resultado del valor obtenido por el usuario a
texto.
"""


else:
    print("Esta opción no es válida. INTENTE DE NUEVO.")

    
"""En esta condicional de "else", la usé por si el usuario no introduce el número
"1" o "2". Sirve para avisar que el valor introducido no es válido.
"""
