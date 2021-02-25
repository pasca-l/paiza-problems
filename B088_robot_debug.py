x_max, y_max = map(int, input().split(" "))
maze = [list(input()) for i in range(x_max)]

# 方向を保持しているdirection_listのインデックスを規格化
def return_direction(direction, integer):
    value = direction + integer
    if value < 0:
        return 3
    elif value > 3:
        return 0
    return value


# マップの範囲内かの確認
def check_range(coord, check):
    if 0 <= coord[0] + check[0] < x_max:
        if 0 <= coord[1] + check[1] < y_max:
            return True
    return False


# ロボット位置の更新
def update(coord, direction):
    direction_list = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    # 直進処理
    check = direction_list[direction]
    if check_range(coord, check):
        if maze[coord[1] + check[1]][coord[0] + check[0]] == ".":
            maze[coord[1] + check[1]][coord[0] + check[0]] = "#"
            coord[0] += check[0]
            coord[1] += check[1]
            return coord, direction
    # 右折処理
    check = direction_list[return_direction(direction, 1)]
    if check_range(coord, check):
        if maze[coord[1] + check[1]][coord[0] + check[0]] == ".":
            direction = return_direction(direction, 1)
            return coord, direction
    # 左折処理
    check = direction_list[return_direction(direction, -1)]
    if check_range(coord, check):
        if maze[coord[1] + check[1]][coord[0] + check[0]] == ".":
            direction = return_direction(direction, -1)
            return coord, direction

    print(coord[0], coord[1])
    return 0, 0


def main():
    coordinate = [0, 0]
    direction = 0
    maze[0][0] = "#"
    while True:
        coordinate, direction = update(coordinate, direction)
        if coordinate == 0:
            break


if __name__ == '__main__':
    main()
