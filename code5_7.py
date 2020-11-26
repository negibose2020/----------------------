# ナップサック問題に対する動的計画法

N=6
W=15
items=[[2,3],[1,2],[3,6],[2,1],[1,3],[5,85]]

dp=[[0 for i in range (W+1)] for j in range (N+1)]

for i in range (N):
    for j in range (W+1):
        if j <items[i][0]:
            dp[i+1][j]=dp[i][j]
        else:
            dp[i+1][j]=max(dp[i][j],dp[i][j-items[i][0]]+items[i][1])


print(dp)