T = int(input())

for test in range(1, T + 1) :
    N, M, K = list(map(int, input().split()))
    arrive = list(map(int, input().split()))
    bread = 0
    for time in range(0, max(arrive) + 1) :
        if time > 0 and time % M == 0 :
            bread += K
        arriving = [i for i, value in enumerate(arrive) if value == time]
        if len(arriving) > 0 :
            bread -= len(arriving)
            if bread < 0:
                print(f"#{test} {'Impossible'}")
                break
            elif time == max(arrive) :
                print(f"#{test} {'Possible'}")