for test_case in range(1, 11):
    count = int(input())
    build_list = list(map(int, input().split()))
    view = 0
    for i in range(0, len(build_list) - 4) :
        five_build = []
        for j in range(0, 5) :
            five_build.append(build_list[i + j])
        if five_build.index(max(five_build)) == 2 :
            five_build.sort()
            view += (five_build[4] - five_build[3])
    print("#" + str(test_case) + " " + str(view))