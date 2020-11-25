def chmin(res,b):
    if res[0]>b:
        res[0]=b
        return True


def rec(i):
    if i==0:
        return 0
    res=[10**5]
    chmin(res,rec(i-1)+abs(h[i]-h[i-1]))
    # print(res)
    if i>1:
        chmin(res,rec(i-2)+abs(h[i]-h[i-2]))
    # print(res)
    return res[0]

N=7
h=[2,9,4,5,1,6,10]
print(rec(N-1))