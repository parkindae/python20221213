# try1.ty
# 함수정의
def divide(a,b):
    return a/b

#에러처리
try:
    #함수호출
    result = divide(5,0)
    
except ZeroDivisionError:
    print("0으로 나누면 안됩니다.")
except TypeError:
    print("숫자여야 연산이 됩니다.")
else:    
    print("결과:{0}".format(result))
finally:
    print("한번 더 체크(이중체크)")

print("전체 코드 실행 종료")


