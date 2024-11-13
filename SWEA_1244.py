T = int(input())
for test_case in range(1, T + 1):
    inputs = list(map(int, input().split()))
    numbers = inputs[0]
    count = inputs[1]
    num_list = []
    max_num_pos = []
    num_str = ""
    for i in str(numbers) :
        num_list.append(int(i))
    num_list_sort = sorted(num_list, reverse=True)
    for k in range(0, len(num_list_sort)):
        if num_list[k] == num_list_sort[0]:
            max_num_pos.append(k)
    max_num_pos.reverse()
    for j in range(0, count) :
        num_list[j], num_list[max_num_pos[j]] = num_list[max_num_pos[j]], num_list[j]
    if count > 1 :
        for l in range(0, count - 1) :
            if num_list[l] == num_list[l + 1] :
                if num_list[max_num_pos[l]] > num_list[max_num_pos[l + 1]]:
                    num_list[max_num_pos[l]], num_list[max_num_pos[l + 1]] = num_list[max_num_pos[l + 1]], num_list[max_num_pos[l]]
    for num in range(0, len(num_list)) :
        num_str += str(num_list[num])
    print("#" + str(test_case) + " " + num_str)