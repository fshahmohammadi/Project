import graph
from collections import deque 
from time import sleep

class Dijkstra:
	def __init__(this, filename = "random", n=6, m=10):
		this.G = graph.WGraph(filename, n, m)
							
	def run(this):
		start = 0
		INF = int(1e9)
		mark = [0 for i in range(this.G.n)]
		par = [-1 for i in range(this.G.n)]
		dis = [INF for i in range(this.G.n)]
		dis[start] = 0
		mst = list()
		while(1):
			k = -1
			m = 1e9
			for i in range(this.G.n):
				if(not mark[i]) and (dis[i] < m):
					k = i
					m = dis[i]
			if(k == -1):
				break
			mark[k] = 1
			if(par[k] != -1):
				mst.append((par[k], k))
			for i in range(len(this.G.a[k])):
				if(dis[this.G.a[k][i]] >  this.G.b[k][i]):
					dis[this.G.a[k][i]] = this.G.b[k][i]
					par[this.G.a[k][i]] = k
		return mst


x = Dijkstra("wsample")
print x.run()
