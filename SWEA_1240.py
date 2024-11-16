T = int(input())

decoding = [['0001101', '0'], ['0011001', '1'], ['0010011', '2'], ['0111101', '3'], ['0100011', '4'],
            ['0110001', '5'], ['0101111', '6'], ['0111011', '7'], ['0110111', '8'], ['0001011', '9']]

for test in range(1, T + 1) :
    N, M = list(map(int, input().split()))
    code = []
    decode_result = []
    sum_odd = 0
    sum_even = 0
    inputs = []
    for i in range(0, N) :
        inputs.append(list(map(str, input().split())))
        if inputs[i][0].count('1') > 0 :
            code = inputs[i][0]
    find_one = [i for i, value in enumerate(code) if value == '1']
    find_one.reverse()
    real_code = code[find_one[0] - 55:find_one[0] + 1]
    
    for j in range(0, 8) :
        decode_num = real_code[j * 7:(j * 7) + 7]
        for decode in range(0, 10) :
            if decode_num == decoding[decode][0] :
                decode_result.append(decoding[decode][1])
                break

    for k in range(0, 4) :
        sum_odd += int(decode_result[k * 2])
        sum_even += int(decode_result[k * 2 + 1])
        if (sum_odd * 3 + sum_even) % 10 == 0 :
            answer = sum_odd + sum_even
        else :
            answer = '0'
    print(f'#{test} {answer}')