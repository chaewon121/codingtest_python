import sys

input = lambda : sys.stdin.readline().rstrip()
#sys.setrecursionlimit(10**6)
n=int(input())
data=list(map(int,input().split()))

data.sort()
result=0
cnt=0
for i in data:
    cnt+=1
    if cnt==i:
        result+=1
        cnt=0
print(result)



'''
[input]
5
2 3 1 2 2
[output]
2

'''