# your code goes here

def main():
	n=int(input())
	mapping={
		"Tetrahedron":4,
		"Cube":6,
		"Octahedron":8,
		"Dodecahedron":12,
		"Icosahedron":20
	}
	ans=0
	while(n>0):
		inp=input()
		ans+=mapping.get(inp)
		n-=1
	print(ans)
main()
