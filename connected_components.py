import graph
from collections import deque 
from time import sleep
from graphDrawer import GraphDrawer
from random import random

class ConnectedComponents:
	def __init__(this, filename = "random", n=6, m=10):
		this.G = graph.Graph(filename, n, m)
		this.draw = GraphDrawer()
		this.draw.init(this.G)
		this.mark = [0 for i in range(this.G.n)]
		this.h = [0 for i in range(this.G.n)]
							
	def run(this, start = 0, end = -1):
		for i in range(this.G.n):
			if not this.mark[i]:
				this.dfs(i, (random(), random(), random()))
	def dfs(this, x, color):
		this.draw.mark(x, 1, (1, 1, 0))
		this.mark[x] = 1
		for i in this.G.a[x]:
			if not this.mark[i]:
				this.dfs(i, color)
		this.draw.mark(x, 1, color)

x = ConnectedComponents("tests/connected_components")
x.run()
