def message_screen(id, group_info, message_info):
    result = []
    for j in message_info:
        if j[0] == id:
            result.append(j[3])
            continue
        if j[1] == 0:
            if j[2] == id:
                result.append(j[3])
                continue
        elif j[1] == 1:
            for i in group_info[j[2]]:
                if i == id:
                    result.append(j[3])
                    continue
    return result


def main():
    first_line = input()
    info = list(map(int, first_line.split(' ')))

    group_info = [list(map(int, input().split(' '))) for i in range(info[1])]
    group_info = dict([(i+1, j[1:]) for i, j in enumerate(group_info)])

    message_info = [input().split(' ') for i in range(info[0])]
    message_info = [[int(i[0]), int(i[1]), int(i[2]), i[3]] for i in message_info]

    for i in range(1, info[0] + 1):
        for j in message_screen(i, group_info, message_info):
            print(j)
        if i == info[0]:
            break
        print("--")

if __name__ == '__main__':
    main()
