n1 = int(input())
n2 = input()

second = n1 * int(n2[2])
first = n1 * int(n2[1])
base = n1 * int(n2[0])
last = n1 * int(n2)

print(second, first, base, last, sep="\n")

# sep를 사용해서 각 콤마 사이에 \n을 추가해줘서
# 하나씩 나오게 할 수 있다.
# 두번째 변수를 str로 받아 인덱스를 지정할 수 있게 했다.
