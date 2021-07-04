"""
Proyecto Básico de Python (Mad Libs / Historias Locas).
Basado en el proyecto de: Kylie Ying (@kylieyying). 
Versión en Español con Modificaciones: Estefania Cassingena Navone (@EstefaniaCassN).
"""
# Concatenar cadenas de caracteres.
# Supongamos que queremos crear una cadena que diga:
# "Aprende a programar con ________."

organización = "freeCodeCamp" # Cadena de caracteres asignada a una variable.

# Algunas alternativas
print("Aprende a programar con " + organización) # Concatenar
print("Aprende a programar con {}".format(organización)) # Método .format()
print(f"Aprende a programar con {organización}") # f-string

# Mad Libs (Historias Locas)

adj = input("Adjetivo: ") # asombroso
verbo1 = input("Verbo: ") # resolver
verbo2 = input("Verbo: ") # programar
sustantivo_plural = input("Sustantivo (plural): ") # metas, objetivos

madlib = f"¡Programar es {adj}! Siempre me emociona porque me encanta {verbo1} problemas. \
¡Aprende a {verbo2} con freeCodeCamp y alcanza tus {sustantivo_plural}!"

print(madlib)
