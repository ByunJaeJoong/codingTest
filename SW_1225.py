<<<<<<< HEAD
for test in range(1, 11) :
    t = int(input())
    password = list(map(int, input().split()))
    if min(password) % 15 == 0 :
        minus = (int(min(password) / 15) * 15) - 15
    else :
        minus = int(min(password) / 15) * 15
    for i in range(0, 8) :
        password[i] -= minus
    for j in range(50) :
        if password[7] <= 0:
            print(f"#{test} {password[0]} {password[1]} {password[2]} {password[3]} {password[4]} {password[5]} {password[6]} 0")
            break
        else :
            password.append(password[0] - (j % 5 + 1))
=======
for test in range(1, 11) :
    t = int(input())
    password = list(map(int, input().split()))
    if min(password) % 15 == 0 :
        minus = (int(min(password) / 15) * 15) - 15
    else :
        minus = int(min(password) / 15) * 15
    for i in range(0, 8) :
        password[i] -= minus
    for j in range(50) :
        if password[7] <= 0:
            print(f"#{test} {password[0]} {password[1]} {password[2]} {password[3]} {password[4]} {password[5]} {password[6]} 0")
            break
        else :
            password.append(password[0] - (j % 5 + 1))
>>>>>>> bb57d6544c4eda3ae293a0d37aa65e202dbb634f
            password.pop(0)