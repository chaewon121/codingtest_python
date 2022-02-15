import sys

input = lambda : sys.stdin.readline().rstrip()
#sys.setrecursionlimit(10**6)
data=list(input())
cnt=0

for i in range(len(data)):

    if i-1>=0:
        if data[i] != data[i - 1]:

            cnt+=1

if cnt%2!=0:
    print(cnt//2+1)
else:
    print(cnt//2)



'''
[input]
0001100
[output]
1

'''