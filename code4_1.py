# code4.1
# 1からNまでの総和を計算する再帰関数
def func41(n):
    if n==0:
        return 0
    return (n)+func41(n-1)

print(func41(10))


# code4.2
# 1からNまでの総和を計算する再帰関数
def func42(n):
    print("func42({})を呼び出しました。".format(n))
    if n==0:
        return 0
    res=n+func42(n-1)
    print("{}までの和 = {}".format(n,res))
    return res

func42(5)