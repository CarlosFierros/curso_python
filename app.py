import argparse
import matplotlib.pyplot as plt
import funciones
 
def main(m: float, b: float):
 
    ''' Funcion principal que calcula las coordenadas de una linea recta
    Recibimos: m y b
    Regresa: nada '''
 
    # m=2.0
    # b=3.0
    # X =[x for x in range(1,11)]
    # Y =[funciones.Calcular_Y(x,m,b) for x in X]
    # print('Enteros:')
    # coordenadas_enteros = list(zip(X,Y))
    # print(coordenadas_enteros)
    plt.plot(X,Y)
    plt.title(f'Linea con pendiente{m} y ordenada al origen {b}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
 
    X = [x/10.0 for x in range(10,110,5)]
    Y = [funciones.Calcular_Y(x,m,b) for x in X]
    coordenadas_flotantes = list(zip(X,Y))
    print('Flotantes')
    print(coordenadas_flotantes)
    plt.plot(X,Y)
    plt.show()
 
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m',type=float, help='Pendiente de la linea', default=2.0)
    parser.add_argument('-b',type=float, help='Ordenada en el origen', default=3.0)
    args = parser.parse_args()
    main(args.m,args.b)
 
    # main(m=2.0,b=3.0)
    # :p