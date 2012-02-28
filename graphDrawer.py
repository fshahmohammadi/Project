from graph import Graph
import math
import time
from shutil import copyfile
import os


class GraphDraw:
	def __init__(this):
		this.fout = open("_Draw.ps", "w")
		this.l = list()
		this.vr = 10

	def cis(this, ang):
		tmp = 0 + 1j
       		return math.cos(ang)+(math.sin(ang))*tmp

	def vertex(this, p):
		this.fout.write(str(p.real) + " " + str(p.imag) + " " + str(this.vr) + " 0 360 arc stroke\n")

	def edge(this, e):
		this.fout.write(str(this.l[e[0]].real) + " " + str(this.l[e[0]].imag) + " moveto\n")
		this.fout.write(str(this.l[e[1]].real) + " " + str(this.l[e[1]].imag) + " lineto\n")
		this.fout.write("stroke\n")

	def mark(this, x, color=(0,0,0)):
		this.fout.write(str(color[0]) + " " + str(color[1]) + " " + str(color[2]) + " setrgbcolor\n")
		p = this.l[x]
		this.fout.write(str(p.real) + " " + str(p.imag) + " " + str(this.vr) + " 0 360 arc fill\n")
		this.Draw()

	def Draw(slef):
		copyfile("_Draw.ps", "Draw.ps")

	def init(this, G):
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
		this.Draw()


tmp = Graph(n=5, m = 10)
G = GraphDraw()
G.init(tmp)
G.mark(0)
time.sleep(5)
G.mark(1)
