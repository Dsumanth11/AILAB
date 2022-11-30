from sys import maxsize
from itertools import permutations
V=4
def TSP(G,s):
	vertex=[]
	for i in range(V):
		if i!=s:
			vertex.append(i)
	MP=maxsize
	NP=permutations(vertex)
	# print(NP)
	# print(vertex)
	for i in NP:
		# print(i)
		CPW=0
		k=s
		for j in i:
			CPW+=G[k][j]
			k=j
		CPW+=G[k][s]
		MP=min(MP,CPW)
	return MP
if __name__=="__main__":
	G=[[0,10,20,32],[12,0,23,15],[13,8,0,21],[12,32,19,0]]
	s=0
	print(TSP(G,s))
 
 