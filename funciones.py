# Archivo con todas las funciones necesarias para la aplicacion "linea"

def calcular_y(x, m, b):
    return m*x + b

def test_linea():
    try:
        assert calcular_y(0, 2, 3) == 3  # Verifica que la función funcione correctamente.
        return True  # Si pasa el test, devuelve True.
    except AssertionError:
        return False  # Si falla el test, devuelve False.
    
if __name__ == '__main__':
    if test_linea():
        print("Todo bien")
    else:
        print("Algo salio mal")