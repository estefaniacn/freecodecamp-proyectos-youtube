"""
Proyecto Básico de Python (Adivina el Número (Computadora)).
Basado en el proyecto de: Kylie Ying (@kylieyying). 
Versión en Español con Modificaciones: Estefania Cassingena Navone (@EstefaniaCassN).
"""
import random

# La computadora debe adivinar el número seleccionado por el jugador.
def adivina_el_número_computadora(x):

    print("============================")
    print("  ¡Bienvenido(a) al Juego!  ")
    print("============================")
    print(f"Selecciona un número entre 1 y {x} para que la computadora intente adivinarlo.")

    # Intervalo de valores válidos
    límite_inferior = 1
    límite_superior = x
    respuesta = ""

    # Miestras el usuario no indique que la respuesta es correcta,
    # continuar el proceso.
    while respuesta != "c":
        # Generar predicción
        if límite_inferior != límite_superior:
            predicción = random.randint(límite_inferior, límite_superior)
        else:
            predicción = límite_inferior  # también podría ser límite_superior porque los límites son iguales.
        
        # Obtener respuesta del usuario
        respuesta = input(f"Mi predicción es {predicción}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcta ingresa (C) ").lower()
        
        if respuesta == "a":
            límite_superior = predicción - 1
        elif respuesta == "b":
            límite_inferior = predicción + 1

    print(f"¡Siii! La computadora adivinó tu número correctamente: {predicción}")


adivina_el_número_computadora(10)
