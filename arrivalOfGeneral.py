nOfSoldiers=int(input())
sequence=list(map(int,input().split(" ")))
maxH=max(sequence)
minH=min(sequence)
maxI=sequence.index(maxH)
minI=nOfSoldiers-sequence[::-1].index(minH)-1
minI=minI+1 if minI<maxI else minI
print(maxI+nOfSoldiers-1-minI)
