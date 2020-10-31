# code4.9 部分和問題を再帰関数を用いる全探索で解く

def func(i,w,a):
    # basecase
    if i==0:
        if w==0:
            return True
        else:
            return False

    if func(i-1,w,a):
        c="選びません"
        print("{}の中の{}を{}。今の合計は{}です。".format(a,a[i-1],c,w))
        return True
    if func(i-1,w-a[i-1],a):
        c="選びます"
        print("{}の中の{}を{}。今の合計は{}です。".format(a,a[i-1],c,w))
        return True
    return False

a=[3,2,6,5]
N=len(a)
W=14

if func(N,W,a):
    print("Yes")
else:
    print("No")