import sys
import time

MOD=1000000
s=0
n=int(sys.stdin.readline())
for i in range(1,n+1):
    factorial=1
    for j in range(1,i+1):
        factorial=factorial*j%MOD
    s=(s+factorial)%MOD
print("%d\n"%s)

print("Time Used=",time.clock())
