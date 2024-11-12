T = int(input())
for test_case in range(1, T + 1):
    inputs = list(map(int, input().split()))
    numbers = inputs[0]
    count = inputs[1]
    num_list = []
    max_num_pos = []
    for i in str(numbers) :
        num_list.append(int(i))
    num_list_sort = sorted(num_list, reverse=True)
    for k in range(0, len(num_list_sort)):
        if num_list[k] == num_list_sort[0]:
            max_num_pos.append(k)
    for j in range(0, count) :
        max_num_pos.reverse()
        print(max_num_pos)
        num_list[j], num_list[max_num_pos[j]] = num_list[max_num_pos[j]], num_list[j]
    if num_list[max_num_pos[0]] :
        
    for m in range(0, count) :
        num_list[max_num_pos[m]]
    print(num_list)


