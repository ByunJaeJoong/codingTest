T = int(input())
for i in range(1, T + 1) :
    inputs = list(map(int, input().split()))
    ingred_num = inputs[0]
    max_cal = inputs[1]
    point = []
    cal = []
    point_com = [0 for _ in range(ingred_num)]
    # print(point_com)
    total_point = []
    for j in range(0, ingred_num) :
        inputs2 = list(map(int, input().split()))
        point.append(inputs2[0])
        cal.append(inputs2[1])
    print(point)
    print(cal)