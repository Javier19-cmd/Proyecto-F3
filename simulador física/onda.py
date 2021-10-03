"""
# AUTORES: ROBERTO FRANCISCO RIOS MORALES , 20979
#          JAVIER SEBASTIÁN VALLE BALSELLS, 20159
#          MARIO DE LEÓN MURALLES         , 19019         
# LABORATORIO DE FISICA 3, SECCION 20
# SIMULACION DE TRAYECTORIA DE UNA PARTICULA A TRAVES DEL CAMPO ELECTRICO GENERADO POR 2 PLACAS CARGADAS V.0.1.
# NOTA: PARA QUE EL PROGRAMA FUNCIONE SE NECESITA TENER MATPLOTLIB INSTALADO
"""
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