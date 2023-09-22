#Al principio, escribo un loop en forma de "while" para iniciar un ciclo donde
#el usuario puede escoger el número de opción que se le indica en la variable
#"qst".

while True:
    qst = int(input("""Introduzca el número de opción que desee usar:
1. Texto a código Morse
2. Código Morse a texto
3. Salir del programa
"""))

#La variable "qst" tiene como función de almacenar el número de opción que
#el usuario va introducir acorde a la opción seleccionada, la opción número
#"3" tiene como uso de cortar el primer ciclo de la opción de escoger el
#programa seleccionado.
    
    if qst >= 1 and qst <= 3:
        if qst == 3:
            break       
    
    #La condicional evalúa que para seguir con el programa, el input definido
    #por el usuario debe de ser 1, 2 o 3.

        while True:
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
                
                texto = str(input("Introduce una letra para ser traducido a\n"
                                  "código morse: ")).lower()
                print("El código morse de este texto es:", txt_a_morse(texto))
                 
            #Si el input definido por el usuario es "1", el progrma continuará
            #con la selección de texto a código morse. El usuario debe de
            #introducir una letra del alfabeto en español para que el output
            #pueda proveer la traducción a código morse.

            #Si el usuario no introduce una letra del alfabeto en español, le
            #aparecerá el mensaje en la consola "El texto no es válido.
            #INTENTE DE NUEVO." Y el ciclo se repetirá hasta que el usuario
            #ingrese un valor que este correcto acorde al programa
            
            if qst == 2:
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
                    
                    
                texto2 = str(input("Introduce un código morse para ser\n"
                                   "traducido a texto: ")).lower()
                print("El texto de este código morse es:", morse_a_txt(texto2))
                
            #Si el input definido por el usuario es "2", el progrma continuará
            #con la selección de código morse a textl. El usuario debe de
            #introducir el código morse de una letra para que el output
            #pueda proveer la traducción al alfabeto en español.

            #Si el usuario no introduce una letra del alfabeto en español, le
            #aparecerá el mensaje en la consola "El texto no es válido.
            #INTENTE DE NUEVO." Y el ciclo se repetirá hasta que el usuario
            #ingrese un valor que este correcto acorde al programa
            
