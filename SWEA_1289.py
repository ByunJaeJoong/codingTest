T = int(input())
for i in range(1, T + 1) :
    origin_mem = input()
    init_mem = origin_mem.replace('1', '0')
    first_one = origin_mem.find('1')
    origin_mem_list = list(origin_mem)
    init_mem_list = list(init_mem)
    for j in range(0, len(origin_mem) - first_one) :
        init_mem_list[first_one + j] = '1'
    print(init_mem_list)