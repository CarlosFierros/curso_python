# Calculo de coordenadas de lineas
def calcular_y(x, m, b):
    return m * x + b

def main():
    m = 2
    b = 3
    X = [x for x in range(1, 11)]
    # Calcula Y elemento por elemento usando la función local calcular_y
    Y = [calcular_y(x, m, b) for x in X]
    print("Enteros: ")
    coordenadas_enteros = list(zip(X, Y))
    print(coordenadas_enteros)

if __name__ == '__main__':
    main()
