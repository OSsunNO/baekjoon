def l(data):
    return len(data)
n = int(input())
a=set()
for i in range(n):
    k=input()
    a.add(k)
a=sorted(list(a))
a=sorted(a,key=l) # python 내장 함수 sort()나 sorted()는 정의한 함수를 key의 인자로 줘서 정의한 함수의 리턴값을 기준으로 정렬을 할 수 있다..!
print(*a,sep='\n')
