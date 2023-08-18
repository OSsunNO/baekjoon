import sys
x = int(input())
n = int(input())
lines = sys.stdin.readlines()
sum = 0
for line in lines:
    a, b = line.rstrip().split()
    sum = int(a)*int(b)
    x -= sum
if(x == 0):
    print("Yes")
else:
    print("No")

