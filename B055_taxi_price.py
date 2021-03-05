import math

def main():
    taxi_num, distance = map(int, input().split(' '))
    param = [list(map(int, input().split(' '))) for i in range(taxi_num)]

    prices = []
    for i in range(taxi_num):
        offset = distance - param[i][0]
        price = math.ceil(offset / param[i][2]) * param[i][3] + param[i][1]
        if offset == 0 or (offset) % param[i][2] == 0:
            price += param[i][3]
        prices.append(price)

    print(min(prices), max(prices))


if __name__ == '__main__':
    main()
