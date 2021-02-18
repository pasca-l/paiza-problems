# score still at 80/100

def check_adjacent(check_pair):
    if abs(check_pair[0] - check_pair[2]) == 1:
        if abs(check_pair[1] - check_pair[3]) == 0:
            return True
    if abs(check_pair[1] - check_pair[3]) == 1:
        if abs(check_pair[0] - check_pair[2]) == 0:
            return True
    return False


def check_atedge(check_pair, max_row, max_column):
    if check_pair[0] == check_pair[2] == 1 or check_pair[0] == check_pair[2] == max_row:
        return True
    if check_pair[1]== check_pair[3]== 1 or check_pair[1] == check_pair[3] == max_column:
        return True
    return False


def generate_dot_adjacent(dot_coordinate, max_row, max_column):
    dot_adjacent = []
    for i in dot_coordinate:
        if i[0] + 1 <= max_row:
            dot_adjacent.append([i[0] + 1, i[1]])
        if i[0] - 1 >= 1:
            dot_adjacent.append([i[0] - 1, i[1]])
        if i[1] + 1 <= max_column:
            dot_adjacent.append([i[0], i[1] + 1])
        if i[1] - 1 >= 1:
            dot_adjacent.append([i[0], i[1] - 1])
    return dot_adjacent


def check_route(check_pair, dot_coordinate):
    card1 = [check_pair[0], check_pair[1]]
    card2 = [check_pair[2], check_pair[3]]
    if card1 in dot_coordinate and card2 in dot_coordinate:
        return True
    return False


def main():
    info = list(map(int, input().split(' ')))
    board = [list(input().split(' ')) for i in range(info[0])]
    check_pair = [list(map(int, input().split(' '))) for i in range(info[2])]
    dot_coordinate = [[i+1, j+1] for i in range(info[0]) for j in range(info[1]) if board[i][j] == "."]
    dot_coordinate = generate_dot_adjacent(dot_coordinate, info[0], info[1])

    for i in check_pair:
        if board[i[0]-1][i[1]-1] != board[i[2]-1][i[3]-1]:
            print("no")
            continue

        if check_adjacent(i):
            print("yes")
            continue
        if check_atedge(i, info[0], info[1]):
            print("yes")
            continue
        if check_route(i, dot_coordinate):
            print("yes")
            continue
        print("no")


if __name__ == '__main__':
    main()
