def main():
    total_days = int(input())
    schedule = list(map(int, input().split(' ')))

    max_counter = 0
    temp_counter = 0
    for i in range(total_days - 6):
        if schedule[i:i+7].count(0) >= 2:
            temp_counter += 1
        else:
            temp_counter = 0

        if temp_counter > max_counter:
            max_counter = temp_counter

    if max_counter > 0:
        max_counter += 6

    print(max_counter)


if __name__ == '__main__':
    main()
