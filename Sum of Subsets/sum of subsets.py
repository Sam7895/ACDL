def SumOfSubSets(index, weight, total): 
	if promising(index, weight): 
		if weight == M: 
			for i in range(N-1): 
				if x[i] == 1: 
					print(W[i+1],end=" ") 
			print("") 
			print('Solution is ', x) 
			print("") 
		else: 
			x[index] = 1 
			SumOfSubSets(index+1, weight + W[index+1], total - W[index+1]) 
			x[index] = 0 
			SumOfSubSets(index+1, weight, total - W[index+1]) 
def promising(index, weight): 
	if index > N-1: 
		return False 
	elif index == N-1: 
		return ((weight + total >= M) and (weight == M)) 
	else: 
		return ( (weight + total >= M) and ( (weight == M) or (weight + W[index+1] <= M) )) 
W = [5,10,12,13,15,18] 
W.insert(0,0) 
N = len(W) 
M = 30 
total = sum(W) 
index = 0 
weight = 0 
x = [0] * (N-1) 
SumOfSubSets(index, weight, total) 