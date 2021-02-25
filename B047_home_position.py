def main():
    string_input = input()

    keyboard = {"q":(0,0), "w":(0,1), "e":(0,2), "r":(0,3), "t":(0,4),
                "y":(0,5), "u":(0,6), "i":(0,7), "o":(0,8), "p":(0,9),
                "a":(1,0), "s":(1,1), "d":(1,2), "f":(1,3), "g":(1,4),
                "h":(1,5), "j":(1,6), "k":(1,7), "l":(1,8),
                "z":(2,0), "x":(2,1), "c":(2,2), "v":(2,3), "b":(2,4),
                "n":(2,5), "m":(2,6)}

    diff_counter = 0
    on_right = True

    for n, i in enumerate(string_input):
        if n == 0:
            if keyboard[i][1] <= 4:
                on_right = not on_right

        if keyboard[i][1] > 4 and not on_right:
            diff_counter += 1
        if keyboard[i][1] <= 4 and on_right:
            diff_counter += 1

        if n + 1 == len(string_input):
            break

        surrounding_coord = [(keyboard[i][0], keyboard[i][1]),
                            (keyboard[i][0] + 1, keyboard[i][1]),
                            (keyboard[i][0] - 1, keyboard[i][1]),
                            (keyboard[i][0], keyboard[i][1] + 1),
                            (keyboard[i][0], keyboard[i][1] - 1)]

        if on_right:
            if keyboard[string_input[n+1]] in surrounding_coord:
                continue
            if keyboard[string_input[n+1]][1] <= 4:
                on_right = not on_right
                continue

        if not on_right:
            if keyboard[string_input[n+1]] in surrounding_coord:
                continue
            if keyboard[string_input[n+1]][1] > 4:
                on_right = not on_right
                continue

    print(diff_counter)


if __name__ == '__main__':
    main()
