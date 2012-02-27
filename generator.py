import random

class GraphGenerator:
	def generate(this, n, m, file = "random.g"):
		fout = open(file, "w")
		e = list()
		for i in range(n):
			for j in range(i, n):
				if(i != j):
					e.append((i, j))
		random.shuffle(e)
		fout.write(str(n) + "\n")
		fout.write(str(m) + "\n")
		for i in range(m):
			fout.write(str(e[i][0]) + " " + str(e[i][1]) + "\n")
	
