def chmin(dp,i,x):
    if dp[i]>x:
        dp[i]=x
        return True
    return False


N=7
h=[2,9,4,5,1,6,10]

INF=10**3
dp=[INF]*N
dp[0]=0

for i in range (N-1):
    chmin(dp,i+1,dp[i]+abs(h[i]-h[i+1]))
    if i<N-2:
        chmin(dp,i+2,dp[i]+abs(h[i]-h[i+2]))
# print(dp)
print(dp[-1])