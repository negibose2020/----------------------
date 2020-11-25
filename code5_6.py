def chmin(res,b):
    if res[0]>b:
        res[0]=b
        return True
    return False


def rec(i):
    # print(memo)
    if i==0:
        return 0
    res=[10**5]
    if memo[i]>-1:
        return memo[i]
    else:
        chmin(res,rec(i-1)+abs(h[i]-h[i-1]))
    if i>1:
        chmin(res,rec(i-2)+abs(h[i]-h[i-2]))
    memo[i]=res[0]
    return res[0]

N=7
h=[2,9,4,5,1,6,10]

memo=[-1]*N
memo[0]=0

print(rec(N-1))