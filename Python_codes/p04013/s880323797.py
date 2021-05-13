MAX_INDEX = 51
MAX_SUM = 2505

dp = [[[-1 for _ in range(MAX_INDEX)] for _ in range(MAX_SUM)] for _ in range(MAX_INDEX)]

def waysutil(index, sum, count, arr, K) : 

	if (index < 0) : 
		return 0; 

	if (index == 0) : 

		if (count == 0) : 
			return 0; 
			
		remainder = sum % count; 

		if (remainder != 0) : 
			return 0; 
			
		average = sum // count; 

		if (average == K) : 
			return 1; 

	if (dp[index][sum][count] != -1) : 
		return dp[index][sum][count]; 

	dontpick = waysutil(index - 1, sum, count, arr, K); 


	pick = waysutil(index - 1, sum + arr[index], count + 1, arr, K); 
						
	total = pick + dontpick; 

	dp[index][sum][count] = total; 
	
	return total; 


def ways(N, K, arr) : 

	Arr = []; 

	Arr.append(-1); 
	for i in range(N) : 
		Arr.append(arr[i]); 

	answer = waysutil(N, 0, 0, Arr, K); 
	return answer; 


n, k = map(int, input().split())
arr = list(map(int, input().split()))
N = len(arr)

print("%d" % (ways(N, k, arr)))
