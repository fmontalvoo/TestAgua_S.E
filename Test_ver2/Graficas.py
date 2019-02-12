import matplotlib.pyplot as pp
import math

class Graficas:

	def __init__(self):
		pass
		
	def graficar(self, p):
		x1 = [0, 10, 15, 25]
		y1 = [0, 1, 1, 0]
		x2 = [25, 35, 40, 50]
		y2 = [0, 1, 1, 0]
		x3 = [50, 56.6, 62.6, 70]
		y3 = [0, 1, 1, 0]
		x4 = [70, 76.6, 82.6, 90]
		y4 = [0, 1, 1, 0]
		x5 = [90, 93.33, 96.33, 100]
		y5 = [0, 1, 1, 0]
		pp.plot(x1, y1,'gray', linewidth=3.0, label='Pesima')
		pp.plot(x2, y2,'red', linewidth=3.0, label='Mala')
		pp.plot(x3, y3,'yellow', linewidth=3.0, label='Regular')
		pp.plot(x4, y4,'green', linewidth=3.0, label='Buena')
		pp.plot(x5, y5,'blue', linewidth=3.0, label='Excelente')
		x = [p, p]
		y = [0 , 1]
		pp.plot(x, y, 'o--', color='black', label='Resultado: '+str(p))
		pp.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, borderaxespad=0.)
		pp.grid(True)
		pp.show()
