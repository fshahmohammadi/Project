import generator

class Graph:
	def __init__(this, filename="random", n=0, m=0):
		filename += ".g"
		if(filename == "random.g"):
			gen = generator.GraphGenerator()
			gen.generate(n, m)
		this.e = list()
		fin = open(filename)
		this.n = int(fin.readline())
		this.m = int(fin.readline())
		this.a = [[] for i in range(this.n)] 
		for i in range(this.m):
			s = fin.readline()
			_t = s.split()
			t = (int(_t[0]), int(_t[1]))
			this.a[t[0]].append(t[1])
			this.a[t[1]].append(t[0])
			this.e.append((t[0], t[1]))
	def output(this):
		print this.a
		print this.e

g = Graph(n=4, m=5)
g.output()