import sys

input = lambda : sys.stdin.readline().rstrip()
#sys.setrecursionlimit(10**6)
n=list(input())
result=0
for i in n:
    a=int(i)
    result=max(result*a,result+a)
print(result)



'''
[input]
02984
[output]
576
[input]
567
[output]
210
'''