#Clase que genera la gráfica de las ondas senosoidales.
import matplotlib.pyplot as plt
from numpy import arange,sin,pi

#Método encargado de poder graficar los datos que recibe.
def ondas(x):

    x=arange(0.0,x*pi,0.01)
    y = sin(x)
    plt.plot(x,y)
    plt.grid(True)
    plt.ylabel("Y")
    plt.xlabel("X")

    plt.show()

    #ondas(x)