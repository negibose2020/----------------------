N=7
h=[2,9,4,5,1,6,10]

INF=10**3
dp=[INF]*N

dp[0]=0
for i in range (1,N):
    if i==1:
        dp[i]=abs(h[i-1]-h[i])
    dp[i]=min(dp[i-1]+abs(h[i-1]-h[i]),dp[i-2]+abs(h[i-2]-h[i]))

# print(dp)
print(dp[-1])