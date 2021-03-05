def main():
    map_width, map_height, log_num = map(int, input().split(' '))
    x, y = map(int, input().split(' '))

    log = [input().split(' ') for i in range(log_num)]

    for i in log:
        if i[0] == 'U':
            for j in range(int(i[1])):
                y += 1
                if y > map_height - 1:
                    y = 0
        if i[0] == 'D':
            for j in range(int(i[1])):
                y -= 1
                if y < 0:
                    y = map_height - 1
        if i[0] == 'R':
            for j in range(int(i[1])):
                x += 1
                if x > map_width - 1:
                    x = 0
        if i[0] == 'L':
            for j in range(int(i[1])):
                x -= 1
                if x < 0:
                    x = map_width - 1

    print(x, y)


if __name__ == '__main__':
    main()
