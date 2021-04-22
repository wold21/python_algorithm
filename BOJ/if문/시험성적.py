# 시험 점수를 입력받아
# 90 ~ 100점은 A
# 80 ~ 89점은 B,
# 70 ~ 79점은 C,
# 60 ~ 69점은 D,
# 나머지 점수는 F
# 를 출력하는 프로그램을 작성하시오.

# print('A' if n1=int(input()) <= 100 and n1 >= 90 else 'B' if n1 <= 89 and n1 >= 80 else 'C' if n1 <= 79 and n1 >= 70 else 'D' if n1 <= 69 and n1 >= 60 else 'F')
n1 = int(input())

if n1 <= 100 and n1 >= 90:
    print('A')
elif n1 <= 89 and n1 >= 80:
    print('B')
elif n1 <= 79 and n1 >= 70:
    print('C')
elif n1 <= 69 and n1 >= 60:
    print('D')
else:
    print('F')
