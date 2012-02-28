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
	
	def getIdx(this, x, y):
		for i in range(len(this.e)):
			if((this.e[i][0] == x and this.e[i][1] == y) or (this.e[i][0] == y and this.e[i][1] == x)):
				return i
		return -1

class WGraph:
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
		this.b = [[] for i in range(this.n)] 
		for i in range(this.m):
			s = fin.readline()
			_t = s.split()
			t = (int(_t[0]), int(_t[1]), int(_t[2]))
			this.a[t[0]].append(t[1])
			this.a[t[1]].append(t[0])
			this.b[t[0]].append(t[2])
			this.b[t[1]].append(t[2])
			this.e.append((t[0], t[1], t[2]))
	def output(this):
		print this.a
		print this.e

