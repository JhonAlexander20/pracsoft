import random

# Función para generar un número secreto
def generar_numero_secreto(minimo, maximo):
    return random.randint(minimo, maximo)

# Función para adivinar el número secreto
def adivinar(numero_secreto, suposicion):
    if suposicion > numero_secreto:
        return "Demasiado alto"
    elif suposicion < numero_secreto:
        return "Demasiado bajo"
    else:
        return "Has ganado!"

# Pruebas
def test_generar_numero_secreto():
    numero_secreto = generar_numero_secreto(1, 100)
    assert 1 <= numero_secreto <= 100

def test_adivinar_demasiado_alto():
    numero_secreto = generar_numero_secreto(1, 100)
    respuesta = adivinar(numero_secreto, 150)
    assert respuesta == "Demasiado alto"

def test_adivinar_demasiado_bajo():
    numero_secreto = generar_numero_secreto(1, 100)
    respuesta = adivinar(numero_secreto, 0)
    assert respuesta == "Demasiado bajo"

def test_adivinar_correcto():
    numero_secreto = generar_numero_secreto(1, 100)
    respuesta = adivinar(numero_secreto, numero_secreto)
    assert respuesta == "Has ganado!"

# Ejecución de las pruebas
if __name__ == "__main__":
    test_generar_numero_secreto()
    test_adivinar_demasiado_alto()
    test_adivinar_demasiado_bajo()
    test_adivinar_correcto()
    print("Todas las pruebas han pasado exitosamente.")
    
    # Parte interactiva del juego
    print("\nBienvenido al juego de adivinanzas!")
    minimo = 1
    maximo = 100
    numero_secreto = generar_numero_secreto(minimo, maximo)
    
    print(f"He generado un número secreto entre {minimo} y {maximo}. ¡Adivina cuál es!")

    while True:
        suposicion = int(input("Introduce tu suposición: "))
        resultado = adivinar(numero_secreto, suposicion)
        print(resultado)
        if resultado == "Has ganado!":
            break
