qst = int(input("""Introduzca el número de opción que desee usar:
1. Texto a código Morse
2. Código Morse a texto
"""))

#En esta variable he guardado un input que el usario tiene que introducir, le
#pide una de las dos opciones que se muestra en el string. He incorporado un
#"int" debido a que el input del usuario tiene que ser un número entero.


if qst == 1:
    def txt_a_morse(txt):
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
        elif txt == " ":
            return "/"
        else:
            return "El texto no es válido. INTENTE DE NUEVO."

    texto = str(input("Introduce un texto para ser traducido a código morse: "))
    
    print("El código morse para este texto es:", txt_a_morse(texto))

#En la primera condicional he decido introducir de igual manera la primera
#condicional que en este caso sería la opción número "1". La función que
#acompaña la condicional se trata de el trabajo que se hara de texto a código
#morse. He guardado dentro de la misma función todas las condicionales que las
#letras del abecedario excepto la letra "ñ". Hasta ahora, mis habilidades en
#Python solo me permiten llegar al punto en el que se puede traducir una
#singular letra a código morse. Al final de la función, la consola imprime
#lo que es el resultado del valor obtenido por el usuario a código morse.


elif qst == 2:
    def morse_a_txt(txt2):
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
        elif txt2 == " ":
            return "/"
        else:
            return "El texto no es válido. INTENTE DE NUEVO."
        
    texto2 = str(input("Introduce un código morse para ser traducido a texto: "))
    
    print("El código morse para este texto es:", morse_a_txt(texto2))

#Esta siguiente condicional es la segunda opción que el usuario puede elegir,
#la condicional es seguida por otra función que en este caso sirve para traducir
#de código morse a texto. Al igual que la función de arriba, este solo puede
#traducir un simple carácter debido a los conocimientos escasos de Python que
#he adquirido durante la materia hasta este punto. Al final de la función la
#consola imprime lo que es el resultado del valor obtenido por el usuario a
#texto.


else:
    print("Esta opción no es válida. INTENTE DE NUEVO.")

#En esta condicional de "else", la usé por si el usuario no introduce el número
#1" o "2". Sirve para avisar que el valor introducido no es válido.

#No entiendo el comentario que recibí de retroalimentación donde dice que el
#código no compila a pesar de quitar los comentarios, o no están introduciendo
#bien los inputs o simplemente ni corren el código.
   

