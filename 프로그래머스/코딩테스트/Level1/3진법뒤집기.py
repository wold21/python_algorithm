def n_ary(n, base):
    result = []
    while n > 0:
        n, r = divmod(n, base)  # 몫이 없어질 때까지 나누기
        result.append(r)  # 나머지를 result에 추가
    return ''.join(map(str, reversed(result)))
    # join 함수를 사용해 result를 뒤집고 하나의 문자열로 바꾼다.


def an_solution(n):
    b3 = n_ary(n, 3)  # n_ary에 10진수와 진법을 보냄
    b3 = b3[::-1]  # 리턴된 문자열을 뒤집는다.
    return int(b3, 3)  # int의 base를 사용해 10진수로 바꾼다.
