<<<<<<< HEAD
import itertools

# arr = [1, 2, 1, 2]
# for i in range(1, 5) :
#     nCr = itertools.combinations(arr, i)
#     print(list(nCr))

# A = [1, 2, 1, 2]
# for i in range(1 << 4):
#     subset_sum = 0
#
#     for j in range(4):
#         print(bin(i), bin(j), bin((1 << j)), bin(i & (1 << j)))
#         if i & (1 << j):
#             subset_sum += A[j]
# sum = 0
# # graph = [[0 for _ in range(100)] for _ in range(100)]
# for i in range(1, 10000) :
#     print(i, i * i + sum)
#     sum += 1 + (2 * (i - 1))
#     if (i * i + sum) > 10000 :
#         break

graph = [[0 for _ in range(72)] for _ in range(72)]
x_sum = 2
y_sum = 0
for y in range(1, 72) :
    for x in range(1, 72) :
        graph[x][y] = x_sum + y_sum
        x_sum += x
=======
import itertools

# arr = [1, 2, 1, 2]
# for i in range(1, 5) :
#     nCr = itertools.combinations(arr, i)
#     print(list(nCr))

# A = [1, 2, 1, 2]
# for i in range(1 << 4):
#     subset_sum = 0
#
#     for j in range(4):
#         print(bin(i), bin(j), bin((1 << j)), bin(i & (1 << j)))
#         if i & (1 << j):
#             subset_sum += A[j]
# sum = 0
# # graph = [[0 for _ in range(100)] for _ in range(100)]
# for i in range(1, 10000) :
#     print(i, i * i + sum)
#     sum += 1 + (2 * (i - 1))
#     if (i * i + sum) > 10000 :
#         break

graph = [[0 for _ in range(72)] for _ in range(72)]
x_sum = 2
y_sum = 0
for y in range(1, 72) :
    for x in range(1, 72) :
        graph[x][y] = x_sum + y_sum
        x_sum += x
>>>>>>> bb57d6544c4eda3ae293a0d37aa65e202dbb634f
print(graph[2][1])