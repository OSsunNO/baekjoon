k = [*map(int,input().split())]; l = int(input())
h = l//3600
m = l%3600//60
s = l%3600%60
k[0] += h; k[1] += m; k[2] += s
if(k[2]>=60):
    k[2] -= 60
    k[1] += 1
if(k[1]>=60):
    k[1] -= 60
    k[0] += 1
if(k[0]>=24):
    k[0] %= 24
print(*k)