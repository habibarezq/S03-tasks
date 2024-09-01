def knapsack(N, W, items):
    # dp array, initialized to 0
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    
    # Fill the dp array
    for weights , values in items:
        print(weights,values)
    
    # The maximum value that can be obtained with capacity W
    return dp[N][W]

# Example Usage:
N = 3  # Number of items
W = 50  # Capacity of knapsack
items=[[3,30],[4,50],[5,60]]

print(knapsack(N, W, weights, values))  # Output: 220

#[weight,value]
#[3,30],[4,50],[5,60]
#[6,5],[5,6],[6,4],[6,6],[3,5],[7,2]
