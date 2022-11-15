# ================================== Start
"""

N M K
a_{1,1} ... a_{1,M}
...
a_{N,1} ... a_{N,M}

-------------

入力例1
3 2 1
2 2
1 2
1 1

出力例1
0
1
2

入力例2
4 5 2
1 3 4 4 5
2 2 2 2 2
1 2 3 4 5
1 1 1 1 1

出力例2
0
5
1
0

"""

N, M, K = map(int, input().split())

for i in range(N):
    a = [int(j) for j in input().split()]
    ans = 0
    for j in range(M):
        if a[j] == K:
            ans += 1
    print(ans)

# ================================== End

# ================================== Start

"""
n 個の数 a_1, … , a_n が与えられます。与えられた数を小さい順に改行区切りで出力



"""


# ================================== End
