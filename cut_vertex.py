import graph
from collections import deque 
from time import sleep
from graphDrawer import GraphDrawer

class CutVertex:
	def __init__(this, filename = "random", n=6, m=10):
		this.G = graph.Graph(filename, n, m)
		this.draw = GraphDrawer()
		this.draw.init(this.G)
		this.mark = [0 for i in range(this.G.n)]
		this.h = [0 for i in range(this.G.n)]
							
	def run(this, start = 0, end = -1):
		for i in range(this.G.n):
			if not this.mark[i]:
				this.dfs(i, 0, i)
	def dfs(this, x, height, root):
		this.mark[x] = 1
		this.draw.mark(x, 1, (0, 0, 1))
		this.h[x] = height
		best = int(1e9)
		bestChild = int(1e9)
		flag = False
		counter = 0
		for i in this.G.a[x]:
			if not this.mark[i]:
				counter = counter + 1
				tmp = this.dfs(i, height + 1, root)
				best = min(best, tmp)
				if(tmp == height):
					flag = True
			else:
				best = min(best, this.h[i])
		if(x == root and counter > 1):
			this.draw.mark(x, 1, (1, 0, 0))
		elif(x != root and flag):
			this.draw.mark(x, 1, (1, 0, 0))
		else:	
			this.draw.mark(x)
		return best

#x = CutVertex("random", n = 5, m = 8)
x = CutVertex("tests/cut_vertex")
x.run()
