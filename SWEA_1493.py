T = int(input())

graph = [[0 for _ in range(300)] for _ in range(300)]
x_sum = 0
first = 1
for y in range(1, 300) :
    for x in range(1, 300) :
        if x == 1 :
            graph[x][y] = first
        else :
            graph[x][y] = graph[x - 1][y] + x + x_sum
    first += y
    x_sum += 1
for test in range(1, T + 1) :
    p, q = list(map(int, input().split()))
    pos1, pos2 = [], []
    for i in range(1, 300) :
        if len(pos1) * len(pos2) > 0 :
            break
        elif p in graph[i]:
            pos1 = [i, graph[i].index(p)]
            if p == q :
                pos2 = pos1
            elif q in graph[i]:
                pos2 = [i, graph[i].index(q)]
        elif q in graph[i]:
            pos2 = [i, graph[i].index(q)]
    print(f'#{test} {graph[pos1[0] + pos2[0]][pos1[1] + pos2[1]]}')