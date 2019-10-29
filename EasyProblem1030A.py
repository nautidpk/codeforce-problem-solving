# your code goes here

def main():
	n=int(input())
	inputs=list(map(int,input().split(" ")))
	ans="EASY"
	for i in inputs:
		if(i):
			ans="HARD"
			break
	print(ans)
	
main()
