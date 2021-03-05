# still at 40/100

def main():
    shop_num, user_num, standard = map(int, input().split(' '))
    my_list = list(map(int, input().split(' ')))
    user_lists = [list(map(int, input().split(' '))) for i in range(user_num)]

    my_favorite_shop = [i for i, n in enumerate(my_list) if n == 3]
    similar_users = []

    for i, n in enumerate(user_lists):
        counter = 0
        for j in my_favorite_shop:
            if n[j] == 3:
                counter += 1

        if counter >= standard:
            similar_users.append(i)

    recommendation = []
    for i in similar_users:
        for j, n in enumerate(user_lists[i]):
            if n == 3:
                recommendation.append(j)

    recommendation = list(set(recommendation))
    for i in my_favorite_shop:
        if i in recommendation:
            recommendation.remove(i)

    result = ' '.join(list(map(lambda x : str(x + 1), recommendation)))
    if result == '':
        print('no')
    else:
        print(result)


if __name__ == '__main__':
    main()
