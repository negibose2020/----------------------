def chmin(dp,i,x):
    if dp[i]>x:
        dp[i]=x
        return True
        # return dp[i]
    return False
    # return dp[i]



def chmin2(dp,i,j,x):
    if dp[i][j]>x:
        dp[i][j]=x
        return True
    return False

