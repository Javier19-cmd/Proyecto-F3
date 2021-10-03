import matplotlib.pyplot as plt
from numpy import arange,sin,pi


def ondas(x):

   #x=arange(0.0,4*pi,0.01)
   y = sin(x)
   plt.plot(x,y)
   plt.grid(True)
   plt.ylabel("Y")
   plt.xlabel("X")
   plt.show()