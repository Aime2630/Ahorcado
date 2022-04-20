import os
import random

palabraMagica = []
letrasEscritas = []
intentos = 3
palabraSecretaAjustes = "1"
nombreArchivoGrupos = "Grupos.txt"

def prepararPalabra(original):
    global palabraMagica
    original = original.lower()
    palabraMagica = []
    for letra in original:
        palabraMagica.append({
            "letra": letra,
            "adivinada": False,
        })

def imprimirPalabra():
    for letraCompuesta in palabraMagica:
        if letraCompuesta["adivinada"]:
            print(letraCompuesta["letra"], end="")
        else:
            print("-", end="")
    print("")

def imprimirPalabraOriginal():
    for letraCompuesta in palabraMagica:
        print(letraCompuesta["letra"], end="")

def descubrirLetra(letraDeUsuario):
    global palabraMagica
    global letrasEscritas
    global intentos
    letraDeUsuario = letraDeUsuario.lower()
    if letraDeUsuario in letrasEscritas:
        return
    else:
        letrasEscritas.append(letraDeUsuario)
    if not letraEstaEnPalabra(letraDeUsuario):
        intentos -= 1
    else:
        for letraCompuesta in palabraMagica:
            if letraCompuesta["letra"] == letraDeUsuario:
                letraCompuesta["adivinada"] = True

def letraEstaEnPalabra(letra):
    global palabraMagica
    for letraCompuesta in palabraMagica:
        if letraCompuesta["letra"] == letra:
            return True
    return False

def imprimirAhorcado():
    if intentos == 1:
        print("""
                       _
                      |   |
                     _O/  |
                      |   |
                     / \  |
                    __|
        """)
    elif intentos == 2:
        print("""
                       ___
                      |   |
                     _O/  |
                      |   |
                          |
                    ______|
                    """)
    
    elif intentos == 3:
        print("""
                       _
                      |   |
                      O   |
                          |
                          |
                    __|
        """)

def dibujarIntentos():
    print("Te quedan " + str(intentos)+ " intentos")

def haGanado():
    global palabraMagica
    for letra in palabraMagica:
        if not letra["adivinada"]:
            return False
    return True



def obtenerPalabra():
    print('')
    print("Seleccione un grupo: \n")
    grupos = obtenerGrupos()
    indice = imprimirGruposYSolicitarIndice(grupos)
    grupo = grupos[indice]
    palabras = obtenerPalabrasDeGrupo(grupo)
    return random.choice(palabras)

def Inicio():
    global letrasEscritas
    global intentos
    intentos = 3
    letrasEscritas = []
    palabra = obtenerPalabra()
    prepararPalabra(palabra)
    while True:
        imprimirAhorcado()
        dibujarIntentos()
        imprimirPalabra()
        descubrirLetra(input("Ingresar letra: "))
        if intentos <= 0:
            print('')
            print("Perdiste. La palabra es:")
            imprimirPalabraOriginal()
            return
        if haGanado():
            print('')
            print("Ganaste, la palabra es:  ", palabra )
            return

def Ajustes():
    if input("Ingrese la contraseña: ") != palabraSecretaAjustes:
        print("Contraseña incorrecta")
        return
    menu = """
1. Crear grupo de palabras
"""

    grupos = obtenerGrupos()
    eleccion = int(input(menu))
    if eleccion <= 0 or eleccion > 3:
        print("No válido")
        return
    elif eleccion == 1:
        crearGrupoDePalabras(grupos)
    

def imprimirGruposYSolicitarIndice(grupos):
    for i, grupo in enumerate(grupos):
        print(f"{i + 1}. {grupo}\n")
    return int(input("Seleccionar grupo: ")) - 1

def crearGrupoDePalabras(grupos):
    grupo = input("Ingrese el nombre del grupo: ")
    palabras = solicitarPalabrasParaNuevoGrupo()
    escribirPalabrasDeGrupo(palabras, grupo)
    grupos.append(grupo)
    escribirGrupos(grupos)
    print("Grupo creado correctamente")

def escribirGrupos(grupos):
    with open(nombreArchivoGrupos, "w") as archivo:
        for grupo in grupos:
            archivo.write(grupo + "\n")

def escribirPalabrasDeGrupo(palabras, grupo):
    with open(grupo + ".txt", "w") as archivo:
        for palabra in palabras:
            archivo.write(palabra + "\n")

def solicitarPalabrasParaNuevoGrupo():
    palabras = []
    while True:
        palabra = input("Ingresar palabra. Sino, deje la cadena vacia para terminar: ")
        if palabra == "":
            return palabras
        palabras.append(palabra)

def modificarGrupoDePalabras(grupos):
    indice = imprimirGruposYSolicitarIndice(grupos)
    grupoQueSeCambia = grupos[indice]
    palabras = obtenerPalabrasDeGrupo(grupoQueSeCambia)
    menu = """
1. Cambiar una palabra
2. Agregar una palabra

Seleccione: """
    eleccion = int(input(menu))
    if eleccion <= 0 or eleccion > 3:
        print("Invalido")
        return
    if eleccion == 1:
        cambiarUnaPalabra(grupoQueSeCambia, palabras)
    elif eleccion == 2:
        agregarUnaPalabra(grupoQueSeCambia, palabras)
    
def cambiarUnaPalabra(grupo, palabras):
    indice = imprimirPalabrasYSolicitarIndice(palabras)
    palabraCambiada = palabras[indice]
    print("Se cambia la palabra " + palabraCambiada)
    nuevaPalabra = input("Ingresar palabra nueva: ")
    palabras[indice] = nuevaPalabra
    escribirPalabrasDeGrupo(palabras, grupo)
    print("Palabra cambiada correctamente")


def agregarUnaPalabra(grupo, palabras):
    palabra = input("Ingrese la palabra que se agrega: ")
    palabras.append(palabra)
    escribirPalabrasDeGrupo(palabras, grupo)
    print("Palabra agregada correctamente")


def imprimirPalabrasYSolicitarIndice(palabras):
    for i, palabra in enumerate(palabras):
        print(f"{i + 1}. {palabra}")
    return int(input("Seleccione la palabra: ")) - 1


def obtenerGrupos():
    grupos = []
    with open(nombreArchivoGrupos) as archivo:
        for linea in archivo:
            linea = linea.rstrip()
            grupos.append(linea)
    return grupos


def obtenerPalabrasDeGrupo(grupo):
    palabras = []
    with open(grupo + ".txt") as archivo:
        for linea in archivo:
            linea = linea.rstrip()
            palabras.append(linea)
    return palabras


def prepararArchivo():
    if not os.path.isfile(nombreArchivoGrupos):
        with open(nombreArchivoGrupos, "w") as archivo:
            archivo.write("")


def menu_principal():
    menu = """ Bienvenidos a mi simulacion del juego Hangman, a continuacion podran visualizar un menu. Por favor seleccione una opcion

1. Inicio
2. Detalles
3. Ajustes
4. Exit

Opcion  seleccionada: """
    eleccion = int(input(menu))
    if eleccion <= 0 or eleccion >= 4:
        exit()
    if eleccion == 1:
        Inicio()

    elif eleccion == 3:
        Ajustes()

def main():
    prepararArchivo()
    while True:
        menu_principal()

main()



