def partition(chocolate, column_num):
    result = []

    for i in chocolate:
        alice = 0
        bob = 0
        counter = 0

        while len(i) > 0:
            if alice <= bob:
                alice += i.pop(0)
                counter += 1
            elif alice > bob:
                bob += i.pop(-1)
        if alice == bob:
            result.append(counter)
        else:
            print("No")
            return

    print("Yes")
    for i in result:
        print("A" * i + "B" * (column_num - i))

    return


def main():
    info = list(map(int, input().split(' ')))
    chocolate = [list(map(int, input().split(' '))) for i in range(info[0])]

    partition(chocolate, info[1])


if __name__ == '__main__':
    main()
