# def knapSack(W, wt, val): 
#     n=len(val)
#     table = [[0 for x in range(W + 1)] for x in range(n + 1)] 
 
#     for i in range(n + 1): 
#         for j in range(W + 1): 
#             if i == 0 or j == 0: 
#                 table[i][j] = 0
#             elif wt[i-1] <= j: 
#                 table[i][j] = max(val[i-1]  
# + table[i-1][j-wt[i-1]],  table[i-1][j]) 
#             else: 
#                 table[i][j] = table[i-1][j] 
   
#     return table[n][W] 
 
# val = [50,100,150,200]
# wt = [8,16,32,40]
# W = 64
 
# print(knapSack(W, wt, val))




def knapsack_recursive(W, weights, values, n, dp):
    if n == 0 or W == 0:
        return 0

    if dp[n][W] != -1:
        return dp[n][W]

    if weights[n - 1] > W:
        return knapsack_recursive(W, weights, values, n - 1, dp)

    inc = value[n - 1] + knapsack_recursive(
        W - weights[n - 1], weights, values, n - 1, dp
    )
    exc = knapsack_recursive(W, weights, values, n - 1, dp)
    dp[n][W] = max(inc, exc)
    return dp[n][W]


def knapsack_tabulation(W, weights, values, n):
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if weights[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(
                    dp[i - 1][j], values[i - 1] + dp[i - 1][j - weights[i - 1]]
                )
    return dp[n][W]


if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    weights, values = [], []
    for i in range(n):
        weight, value = map(
            int, input(f"Enter weight and value for item {i + 1}: ").split()
        )
        weights.append(weight)
        values.append(value)

    W = int(input("Enter the maximum weight of knapsack: "))
    print(knapsack_tabulation(W, weights, values, n))




