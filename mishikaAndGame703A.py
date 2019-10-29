# your code goes here

def main():
	n=int(input())
	ans=[0,0]
	while(n>0):
		m,c=map(int,input().split(" "))
		if(m>c):
			ans[0]+=1
		elif(c>m):
			ans[1]+=1
		n-=1
	if(ans[0]==ans[1]):
		print('Friendship is magic!^^')
	else:
		print('Mishka' if ans[0] > ans[1] else 'Chris')
main()
