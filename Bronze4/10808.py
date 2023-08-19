s = input()
dict = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,
        'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0,}
for i in range(len(s)):
    if(s[i] in dict):
        dict[s[i]] += 1
print(*dict.values())

# 다른 풀이
arr=input()
cnt=[0]*26 # 0이 26개 채워진 배열 생성
for i in arr:
    # ord()는 문자를 숫자로, chr()는 숫자를 문자로, bin()는 숫자를 2진수로 각각 반환하는 함수
    # 'a'부터 ord() 값이 97, 98, ...이므로 ord(i)-97을 통해 배열 인덱스 값 도출 후 각 요소에 접근
    cnt[ord(i)-97]+=1
print(*cnt)