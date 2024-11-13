for test_case in range(1, 11) :
    dump = int(input())
    box = list(map(int, input().split()))
    for i in range(0, dump) :
        box.sort(reverse=True)
        box[0] -= 1
        box[len(box) - 1] += 1
    box.sort(reverse=True)
    answer = str(box[0] - box[len(box) - 1])
    print("#" + str(test_case) + " " + answer)