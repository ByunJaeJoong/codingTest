T = int(input())
for i in range(1, T + 1) :
    farm_size = int(input())
    farm_value = [list(map(str, input().split())) for _ in range(farm_size)]
    profit = 0
    middle = int(farm_size / 2)
    for j in range(0, middle) :  
        for k in farm_value[j][0][middle - j:farm_size - middle + j] :
            profit += int(k)          
        for l in farm_value[farm_size - 1 - j][0][middle - j:farm_size - middle + j] :
            profit += int(l)
    for m in farm_value[middle][0] :
        profit += int(m)
    print("#" + str(i) + " " + str(profit))