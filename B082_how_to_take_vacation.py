import copy

def count_longest(inputlist):
    max_count = 0
    counter = 0
    index = 0
    for i in range(len(inputlist)):
        if inputlist[i] == 0:
            counter += 1
        elif inputlist[i] == 1:
            counter = 0
        if max_count < counter:
            max_count = counter
    return max_count


def change_schedule(inputlist, daysoff, shiftvalue):
    possibility = inputlist.copy()
    countdown = daysoff
    for i in range(shiftvalue, len(inputlist)):
        if countdown <= 0:
            break
        if possibility[i] == 1:
            possibility[i] = 0
            countdown -= 1
    return possibility


def main():
    first_line = input()
    days = list(map(int, first_line.split(' ')))
    #0 = 'off', 1 = 'work'
    schedule = [0 if input() == 'off' else 1 for i in range(days[0])]

    max_daysoff = 0
    for i in range(days[0] - days[1]):
        check = count_longest(change_schedule(schedule, days[1], i))
        if max_daysoff < check:
            max_daysoff = check
    print(max_daysoff)


if __name__ == '__main__':
    main()
