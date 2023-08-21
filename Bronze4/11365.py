while(1):
    n = input()
    if (n == 'END'): break
    n = list(n)
    for i in range(len(n)-1,-1,-1):
        n.append(n[i])
        del n[i]
    print(*n,sep='')

# 다른 풀이 1 - '구분자'.join(리스트) 함수 사용,
# 매개변수로 들어온 리스트의 각 요소들 사이에 구분자를 넣어 하나의 문자열로 합쳐서 반환
# reversed를 사용해 거꾸로 루프를 돌림 - ex) for letter in reversed(letters): 이런 식으로 사용가능
while 1:
    t=input()
    if t=="END":
        break
    else:
        print("".join(reversed(t)))

# 다른 풀이 2 - 슬라이싱 이용
while True :
    a=input()
    if a=='END' :
        break
    print(a[::-1])