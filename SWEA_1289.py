T = int(input())
for i in range(1, T + 1) :
    origin_mem = input()
    init_mem = origin_mem.replace('1', '0')
    origin_mem_list = list(origin_mem)
    init_mem_list = list(init_mem)
    mem_len = len(origin_mem)
    find_one = [i for i, value in enumerate(origin_mem_list) if value == '1']
    sliced_list = origin_mem_list[find_one[0]: mem_len + 1]
    find_zero = [i + find_one[0] for i, value in enumerate(sliced_list) if value == '0']
    count = 0
    print(find_one, find_zero)
    # for k in range(0, mem_len) :

    for j in range(0, mem_len) :
        if init_mem_list[find_one[j]] == '0' :
            array_one = ['1' for _ in range(mem_len - find_one[j])]
            init_mem_list[find_one[j]: mem_len] = array_one
            count += 1
            # print(init_mem_list)
            if init_mem_list == origin_mem_list :
                print('#' + str(i) + ' ' + str(count))
                break
            else :
                array_zero = ['0' for _ in range(mem_len - find_zero[j])]
                init_mem_list[find_zero[j]: mem_len] = array_zero
                count += 1
                # print(init_mem_list)
                if init_mem_list == origin_mem_list :
                    print('#' + str(i) + ' ' + str(count))
                    break