# code4.5 フィボナッチ数列を求める再帰関数
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    
    return (fib(n-1)+fib(n-2))

# print(fib(9))


# code4.6 フィボナッチ数列を求める再帰関数の再帰呼び出しの様子
def fib2(n):
    print("fib2({})を呼び出しました。".format(n))
    if n==0:
        return 0
    elif n==1:
        return 1

    res =fib2(n-1)+fib2(n-2)
    print("第{}項目は、{}です。".format(n,res))
    return res

# fib2(6)

# code4.7 フィボナッチ数列をfor文による反復で求める
def fibFor(n):
    F=[0,1]
    for i in range (2,50):
        f=F[i-1]+F[i-2]
        F.append(f)
        print("{}項目は、{}です。".format(i,f))

# fibFor(50)

# code4.8 フィボナッチ数列を求める再帰関数をメモ化
def fibmemo(n):
    # memo=[-1]*(n+1)
    memo[0]=0
    memo[1]=1
    print(memo)
    if memo[n]!=-1:
        return memo[n]
    else:
        f=fibmemo(n-1)+fibmemo(n-2)
        memo[n]=f
        return f

N=30
memo = [-1]*(N+1)

a=fibmemo(N)
print(a)
print(memo)