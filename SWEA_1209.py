for i in range(1, 11) :
    test_case = int(input())
    numbers_list = [list(map(int, input().split())) for _ in range(100)]
    sum_list = []
    sum_cross1 = 0
    sum_cross2 = 0
    for a in range(0, 100) :
        sum_list.append(sum(numbers_list[a]))
        sum_col = 0
        sum_cross1 += numbers_list[a][a]
        sum_cross2 += numbers_list[a][99 - a]
        for b in range(0, 100) :
            sum_col += numbers_list[b][a]
        sum_list.append(sum_col)
    sum_list.append(sum_cross1)
    sum_list.append(sum_cross2)
    print('#' + str(i) + ' ' + str(max(sum_list)))