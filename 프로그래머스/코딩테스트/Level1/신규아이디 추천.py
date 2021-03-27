def solution(new_id):
    delStr = ''
    new_id = new_id.lower()
    new_id = list(new_id)
    for char in new_id:
        if char.isalnum() or char in '-_.':
            delStr += char
    print(delStr)

    while '..' in delStr:
        delStr = delStr.replace('..', '.')
    print(delStr)

    if delStr.startswith('.'):
        delStr = delStr[1:]
    if delStr.endswith('.'):
        delStr = delStr[:-1]
    print(delStr)

    if len(delStr) == 0:
        delStr += 'a'
    print(delStr)

    if len(delStr) >= 16:
        delStr = delStr[:15]
        if delStr.endswith('.'):
            delStr = delStr[:-1]
    print(delStr)

    if len(delStr) <= 3:
        delStr = delStr + delStr[-1] * (3-len(delStr))

    return delStr


new_id = "=.="

print(solution(new_id))
