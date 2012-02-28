import graph
from collections import deque 
from time import sleep
from graphDrawer import GraphDrawer

class BFS:
	def __init__(this, filename = "random", n=6, m=10):
		print filename
		this.G = graph.Graph(filename, n, m)
		this.draw = GraphDrawer()
		this.draw.init(this.G)
		this.q = deque()
							
	def run(this, start = 0, end = -1):
		if(end == -1):
			end = this.G.n-1
		this.draw.mark(end, 0, (0, 0, 1))
		this.draw.mark(start, 1, (0, 1, 0))
		mark = [0 for i in range(this.G.n)]
		par = [-1 for i in range(this.G.n)]
		this.q.append(start)
		mark[start] = 1
		this.draw.mark(start, 0)
		while(this.q):
			if(mark[end]):
				break
			x = this.q.pop()
			this.draw.mark(x, 1, (1, 0, 0))
			for i in this.G.a[x]:
				if not mark[i]:
					mark[i] = 1
					this.draw.mark(i)
					par[i] = x
					this.q.append(i)
					if(i == end):
						break
			this.draw.mark(x, 0)
					
		if not mark[end]:
			return None
		path = list()
		while(end != -1):
			path.append(end)
			end = par[end]
		for i in range(len(path)-1):
			this.draw.markEdge(this.G.getIdx(path[i], path[i+1]), 0, (0, 1, 1))


#x = BFS("random", n = 5, m = 8)
x = BFS("path")
x.run()
