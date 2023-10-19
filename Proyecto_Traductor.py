"""
Eduardo Hernández Alonso - A01707225
19 de octubre de 2023
Proyecto Libre Python
Traductor de Código Morse.
El programa recibe el texto del usuario y lo traduce a código morse, también
puede recibir múltiples código morse y traducirlos a texto, igualmente cuenta
con otras tres opciones donde el usuario puede hacer operaciones aritméticas de
dos números, que en este caso son: suma, multiplación y división. Y el
resultado de estos dos números es traducido a código morse.
"""

#Bibliotecas
import random

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
============================ Funciones para la traducción =====================
"""

def traduccion_texto(palabra):

    """
    (Uso de funciones, ciclos, condicionales y condicionlaes anidadas)
    Recibe: palabra
    Hace la traducción de texto a código morse mediante usando ciclos que
    revisen la función datos() donde los elementos son guardados y da como
    resultado un texto totalemente traducido sin importar las mayúsculas
    o minúsculas y separando cada código morse con una diagonal "/".
    Devuelve: Código morse traducido del texto
    """
    
    codigo_morse_letras, codigo_morse_especiales = datos()

    texto = " "
    
    for x in palabra.upper():
        if x == " ":
            texto = texto + "/"
        else:
            for morse, letra in codigo_morse_letras:
                if letra == x:
                    texto = texto + morse + " "
                    
            for morse, caracter in codigo_morse_especiales:
                if caracter == x:
                    texto = texto + morse + " "
                    

    return texto.strip()

def traduccion_morse(texto_morse):

    """
    (Uso de funciones, ciclos, ciclos anidados, condicionales y
    condicionlaes anidadas)
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
                    
            for morse, caracter in codigo_morse_especiales:
                if caracter == morse:
                    texto = texto + caracter
                    
            texto = texto + ""
    
    return texto.strip()

"""
=============================== Funciones operadoras ==========================
"""

def suma_morse():

    """
    (Uso de funciones y operadores)
    La función hace la sumas de dos números que son ingresados por el usuario,
    esta suma se guarda en otra variable de tipo string para luego ser
    convertido en código morse con la función "traduccion_texto(palabra)".
    """
    
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))

    suma_str = str(numero1 + numero2)
    morse_suma = traduccion_texto(suma_str)

    return morse_suma

def multiplicacion_morse():
    
    """
    (Uso de funciones y operadores)
    La función hace la multiplicación de dos números que son ingresados
    por el usuario, esta mutliplicación se guarda en otra variable de tipo
    string para luego ser convertido en código morse con la función
    "traduccion_texto(palabra)".
    """
    
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))

    mult_str = str(numero1 * numero2)
    morse_mult = traduccion_texto(mult_str)

    return morse_mult

def division_morse():

    """
    (Uso de funciones y operadores)
    La función hace la división de dos números que son ingresados por el
    usuario, esta división se guarda en otra variable de tipo string para
    luego ser convertido en código morse con la función
    "traduccion_texto(palabra)"
    """
    
    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))

    div_str = str(numero1 / numero2)
    morse_div = traduccion_texto(div_str)

    return morse_div
    
"""
=============================== Menú del programa =============================
"""

def menu():

    """
    (Uso de funciones, ciclos y condicionales)
    Inicializa el menú dando al usuario libertad de ingresar un número
    del 1 al 6, donde cada uno tiene un diferente resultado, el usuario puede
    seguir usando el programa hasta que este ingrese la opcion número 6 donde
    el programa se cierra y manda a imprimir un mensaje aleatorio despidiendo
    al usuario.
    """
    
    while True:
        print("\nMenú:")
        print("1) Traductor de Texto a Código Morse")
        print("2) Traductor de Código Morse a Texto")
        print("3) Sumar dos números y convertir a código Morse")
        print("4) Multiplicar dos números y convertir a código Morse")
        print("5) Dividir dos números y convertir a código Morse")
        print("6) Salir\n")

        opcion = input("Elija una opción del 1 al 6: ")

        if opcion == "1":
            frase = input("Ingrese un texto: ")
            morse = traduccion_texto(frase)
            print("La traducción del texto a código Morse es:\n", morse)
            
        elif opcion == "2":
            morse = input("(ÚNICAMENTE INGRESE LETRAS)"
                          "\n(Separe cada código morse con un espacio)"
                          "\nIngrese un código Morse: ")
            texto = traduccion_morse(morse)
            print("La traducción de código Morse a texto es:\n", texto)
            
        elif opcion == "3":
            suma = suma_morse()
            print("La suma convertida a código Morse es:\n", suma)
            
        elif opcion == "4":
            mult = multiplicacion_morse()
            print("La multiplicación convertida a código Morse es:\n", mult)
            
        elif opcion == "5":
            div = division_morse()
            print("La división convertida a código Morse es:\n", div)
            
        elif opcion == "6":
            despedidas = ["¡Adiós!", "¡Hasta luego!",
                          "¡Adiós, que tengas un buen día!",
                          "¡Hasta la vista!",
                          "Gracias por usar este programa.",
                          "¡Hasta siempre!"]
            print(random.choice(despedidas)) #Mensaje de despedida aleatorio
            break
        
        else:
            print("Opción incorrecta. INTENTE DE NUEVO.")

menu()
