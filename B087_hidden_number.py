# still at 60/100
# run time error for 3 tests

def main():
    height, width, digit = map(int, input().split(' '))
    grid = [list(input()) for i in range(height)]

    candidate = []
    for i in grid:
        candidate.append(''.join(i))

    for i in range(width):
        ver_str = ''
        for j in grid:
            ver_str += j[i]
        candidate.append(ver_str)

    max_num = 0
    for i in candidate:
        for start in range(width - digit + 1):
            check_num = int(i[start : start+digit])
            if check_num > max_num:
                max_num = check_num

    print(max_num)


if __name__ == '__main__':
    main()
