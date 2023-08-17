# Way 1 - EOF 예외 처리를 통해 파일의 끝을 판단하고 break 걸기
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)

    except EOFError: # EOF(End of File) - 파일의 끝을 판단해서 프로그램을 종료해야함
        break

# Way 2 - sys.stdin.readlines() 메서드를 통해 파일의 끝까지 가져오고 줄 단위 처리하는 방식
# import sys
#
# lines = sys.stdin.readlines()
#
# for line in lines:
#     A, B = map(int, line.split())
#     print(A+B)