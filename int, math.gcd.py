# 곱하기와 정수
def solution(num1, num2):
    answer = int((num1 / num2) * 1000) # 정수 int()
    return answer

#####################################################

# 분수의 합
import math

def solution(numer1, denom1, numer2, denom2):
    b = denom1 * denom2 # 분모
    a = (numer1 * denom2) + (numer2 * denom1) # 분자
    
    gcd = math.gcd(a, b) # 기약분수 만드는 함수
    a = a // gcd
    b = b // gcd
    answer = [a, b]
    return answer
