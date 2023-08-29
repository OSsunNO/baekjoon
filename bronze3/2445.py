n=m=int(input())
while(l:=abs(n:=n-1))<m:
    print('*'*(m+~l+1)+' '*(2*l)+'*'*(m+~l+1))
