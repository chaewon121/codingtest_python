import sys

input = lambda : sys.stdin.readline().rstrip()
#sys.setrecursionlimit(10**6)


n,m=map(int,input().split())
data=list(map(int,input().split()))
table=[0]*(m+1)
for i in data:
    table[i]+=1

result=n*(n-1)//2
for i in table:
    result-= i*(i-1)//2
print(result)


'''
[input]
5 3
1 3 2 3 2
[output]
8
[input]
8 5
1 5 4 3 2 4 5 2
[output]
25
'''