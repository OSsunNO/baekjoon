while(1):
    a=[*map(int,input().split())]
    if(a[0]==a[1]==a[2]==0):
        break
    if(((max(a)**2)-(min(a)**2))**(1/2) in a):
        print('right')
    else: print('wrong')

# 다른 풀이 - 리스트 할당이 아닌 각 변수 a,b,c에 정렬된 입력값을 할당하고 슬라이싱을 이용해 wrong과 right 출력
while(1):
    a,b,c = sorted(map(int,input().split()))
    if(a==b==c==0):break;
    else:print(['wrong','right'][a*a+b*b==c*c])