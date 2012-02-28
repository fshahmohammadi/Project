from graph import Graph
import math


class GraphDraw:
	def __init__(this):
		this.fout = open("Draw.ps", "w")
		this.l = list()

	def cis(this, ang):
		tmp = 0 + 1j
       		return math.cos(ang)+(math.sin(ang))*tmp

	def vertex(this, p, r = 10):
#		this.fout.write(str(p.real) + " " + str(p.imag) + " moveto\n")
		this.fout.write(str(p.real) + " " + str(p.imag) + " " + str(r) + " 0 360 arc stroke\n")
	def edge(this, e):
		this.fout.write(str(this.l[e[0]].real) + " " + str(this.l[e[0]].imag) + " moveto\n")
		this.fout.write(str(this.l[e[1]].real) + " " + str(this.l[e[1]].imag) + " lineto\n")
		this.fout.write("stroke\n")

	def Draw(this, G):
		this.fout.write("newpath\n")
		ang = 2*math.pi / G.n
		center = 300 + 400j
		r = 200
		for i in range(G.n):
			this.l.append(center + r * this.cis(i * ang))
		for i in this.l:
			this.vertex(i)
		for i in G.e:
			this.edge(i)


tmp = Graph(n=5, m = 10)
G = GraphDraw()
G.Draw(tmp)
