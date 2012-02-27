import graph
from collections import deque 
from time import sleep

class BFS:
	def __init__(this, filename = "random", n=6, m=10):
		this.G = graph.Graph(filename, n, m)
		this.q = deque()
							
	def run(this, start = 0, end = -1):
		if(end == -1):
			end = this.G.n-1
		mark = [0 for i in range(this.G.n)]
		par = [-1 for i in range(this.G.n)]
		this.q.append(start)
		mark[start] = 1
		while(this.q):
			x = this.q.pop()
			for i in this.G.a[x]:
				if not mark[i]:
					mark[i] = 1
					par[i] = x
					this.q.append(i)
					
		if(par[end] == -1):
			return None
		path = list()
		while(end != -1):
			path.append(end)
			end = par[end]
		return path


x = BFS("sample")
print x.run()
