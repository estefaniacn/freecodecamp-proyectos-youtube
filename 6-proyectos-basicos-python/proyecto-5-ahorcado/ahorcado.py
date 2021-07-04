"""
Proyecto Básico de Python (El Ahorcado).
Basado en el proyecto de: Kylie Ying (@kylieyying). 
Versión en Español con Modificaciones: Estefania Cassingena Navone (@EstefaniaCassN).
"""
import random
import string

from palabras import palabras
from ahorcado_diagramas import vidas_diccionario_visual


def obtener_palabra_válida(palabras):
    palabra = random.choice(palabras)  # seleccionar una palabra al azar de la lista

    # Si la palabra contiene un guión o un espacio,
    # seguir seleccionando una palabra al azar.
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()


def ahorcado():

    print("=======================================")
    print(" ¡Bienvenido(a) al juego del Ahorcado! ")
    print("=======================================")

    palabra = obtener_palabra_válida(palabras)
    letras_por_adivinar = set(palabra)  # conjunto de letras de la palabra que deben ser adivinadas.
    abecedario = set(string.ascii_uppercase) # conjunto de letras en el abecedario.
    letras_adivinadas = set()  # letras que el usuario ha advinado durante el juego.

    vidas = 7

    # Obtener respuesta del usuario mientras existan 
    # letras pendientes y al jugador le queden vidas.
    while len(letras_por_adivinar) > 0 and vidas > 0:
        # Letras adivinadas:
        # ' '.join(['a', 'b', 'c']) --> 'a b c'
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")

        # Estado actual de la palabra que el jugador debe adivinar (por ejemplo:  H - L A)
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        print(vidas_diccionario_visual[vidas]) # mostrar estado del ahorcado.
        print(f"Palabra: {' '.join(palabra_lista)}") # mostrar las letras separadas por un espacio.

        # El usuario escoge una letra nueva
        letra_usuario = input('Escoge una letra: ').upper()

        # Si la letra escogida por el usuario está en el abecedario
        # y no está en el conjunto de letras que ya se han ingresado,
        # se añade la letra al conjunto de letras ingresadas.
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
            # Si la letra está en la palabra, quitar la letra 
            # del conjunto de letras pendientes por adivinar. 
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            # Si la letra no está en la palabra, quitar una vida.
            else:
                vidas = vidas - 1
                print(f"\nTu letra, {letra_usuario} no está en la palabra.")
        # Si la letra escogida por el usuario ya fue ingresada.
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra. Por favor escoge una letra nueva.")
        else:
            print("\nEsta letra no es válida.")

    # El juego llega a esta línea cuando se agotan las vidas del jugador 
    # o cuando se adivinan todas las letras de la palabra.
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"¡Ahorcado! Perdiste. Lo lamento mucho. La palabra era: {palabra}")
    else:
        print(f'¡Excelente! ¡Adivinaste la palabra {palabra}!')


if __name__ == '__main__':
    ahorcado()