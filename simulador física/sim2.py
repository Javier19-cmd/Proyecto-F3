"""
# AUTORES: ROBERTO FRANCISCO RIOS MORALES, 20979
#          JAVIER SEBASTIÁN VALLE BALSELLS, 20159
#          MARIO DE LEÓN MURALLES         , 19019         
# LABORATORIO DE FISICA 3, SECCION 20
# SIMULACION DE TRAYECTORIA DE UNA PARTICULA A TRAVES DEL CAMPO ELECTRICO GENERADO POR 2 PLACAS CARGADAS V.0.1.
# NOTA: PARA QUE EL PROGRAMA FUNCIONE SE NECESITA TENER MATPLOTLIB INSTALADO
"""

# Librerías a usar.
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from onda import ondas
from nuevo import nuevo   #Mix de 2D a 3D

#Segunda gráfica a revisar.
#Esta gráfica es la que pertenece al movimiento de la partícula en el plano xz.
def plano_xz(vep):

    print("\nSIMULADOR DE MOVIMIENTO DE PARTICULAS A TRAVES DE UN CAMPO ELECTRICO\n")
    
    # INPUT
    q = 30
    q = q*-1.602*10**(-19) # C

    m = 50
    m = m*10**(-31) # kg

   # vep = float(input("\nIngrese el voltaje entre placas (en V): ")) #Se le pide al usuario el voltaje de la primera gráfica.
    #vep2 = float(input("\nIngrese el voltaje entre placas (en V): ")) ##Se le pide al usuario el voltaje de la segunda gráfica.

    vox = 45
    vox = vox*10**5
    
    # INITIAL VALUES
    x = 0
    d = 0.03 # 3 cm
    y = 0.015

    #z = 0.015 #Dato de la segunda gráfica.

    # DATA LIST
    ys = []
    xs = []

    #zs = [] #Segunda gráfica.
    
    # LOGIC PROCESS 
    while x <= 0.03:
        xs.append(x)
        ys.append(y)
        #zs.append(z) #Segunda gráfica.
        dy = ((q*vep)/(2*m*d))*((x/vox)**2)

        #dz = ((q*vep2)/(2*m*d))*((x/vox)**2) #Segunda gráfica.
        x = x + 0.001
        y = y + dy
        #z = z + dz #Segunda gráfica.
        t = (x/vox)*10**9
        if y < 0 or y > 0.03:
            break
    
    # DEFINE GRAPH AND AXIS
    graph = plt.figure()
    ax = graph.gca()
    
    # DEFINE A FUNCTION TO ANIMATE THE GRAPH
    def act(i):
        ax.clear()
        ax.scatter(xs[:i], ys[:i])
        text = ax.text(0.025, 0.025, "Tiempo de vuelo: " + '%.2f' % t + " ns", bbox = {'facecolor': 'gray', 'alpha': 0.5, 'pad': 3})
        plt.xlim(0, 0.03)
        plt.ylim(-0.005, 0.035)
        plt.title("Movimiento de una partícula con carga a través de un campo eléctrico generado por dos placas cargadas")
        plt.xlabel("Desplazamiento horizontal (m)")
        plt.ylabel("Desplazamiento vertical (m)")
        plt.axhspan(0.030, 0.035, color = "gray")
        plt.axhspan(-0.005, 0, color = "gray")

    # ANIMATED OUTPUT
    anim = ani.FuncAnimation(graph, act, range(len(xs)), interval=t, repeat=False)
    
    #anim2 = ani.FuncAnimation(graph, act, range(len(zs)), interval=t, repeat=False) #Segunda gráfica.
    
    #plt.plot(len(xs),t)

    plt.show()
    ondas(t) #Ondas ya generadas.
    nuevo(t) #Mandando datos del voltaje a la clase de 3D.

#plano_xz()