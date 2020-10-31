# code4.4
# ユークリッドの互除法によって最大公約数を求める

def gcd(m,n):
    if n==0:
        return m
    return gcd(n,m%n)

print(gcd(15,51))