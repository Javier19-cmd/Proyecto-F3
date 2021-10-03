#Segunda gráfica a revisar.
def plano_xz():

    # INPUT
    q = 30
    q = q*-1.602*10**(-19) # C

    m = 50
    m = m*10**(-31) # kg

    vepy = float(input("\nIngrese el voltaje entre placas (en V): "))

    vox = 45
    vox = vox*10**5
    
    # INITIAL VALUES
    x = 0      # posicion inicial
    d = 0.3    # 30 cm
    y = 0.15   # 15 cm 

    # DATA LIST
    vs = []
    ws = []

    # LOGIC PROCESS 
    while x <= 0.3:
        vs.append(x)
        ws.append(y)
        dy = ((q*vepy)/(2*m*d))*((x/vox)**2)
        x = x + 0.001
        y = y + dy
        a = (x/vox)*10**9
        

    # DEFINE GRAPH AND AXIS
    graph = plt.figure()
    ax = graph.gca()
    
    # DEFINE A FUNCTION TO ANIMATE THE GRAPH
    def act(i):
        ax.clear()
        ax.scatter(vs[:i], ws[:i])
        text2 = ax.text(0.025, 0.025, "Tiempo de vuelo: " + '%.2f' % a + " ns", bbox = {'facecolor': 'gray', 'alpha': 0.5, 'pad': 3})
        plt.xlim(0, 0.03)
        plt.ylim(-0.005, 0.035)
        plt.title("Movimiento de una partícula con carga a través de un campo eléctrico generado por dos placas cargadas")
        plt.xlabel("Desplazamiento horizontal (m)")
        plt.ylabel("Desplazamiento vertical (m)")
        plt.axhspan(0.030, 0.035, color = "gray")
        plt.axhspan(-0.005, 0, color = "gray")

    # ANIMATED OUTPUT
    anim2 = ani.FuncAnimation(graph, act, range(len(ws)), interval=a, repeat=False)
    plt.show()

plano_xz()