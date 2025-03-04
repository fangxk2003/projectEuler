# def dfs(id, cnt, o) :
#     if (id == 8) :
#         if (o and cnt == 4) :
#             global res
#             res += 1
#         return
#     dfs(id + 1, cnt, o or (id + 1 - cnt > cnt))
#     if (cnt < 4) : dfs(id + 1, cnt + 1, o)

# res = 0
# dfs(1, 1, 0)
# print(res)


# def dfs(id, cnt, o) :
#     if (id == 10) :
#         if (o and cnt == 5) :
#             global res
#             res += 1
#         return
#     dfs(id + 1, cnt, o or (id + 1 - cnt > cnt))
#     if (cnt < 5) : dfs(id + 1, cnt + 1, o)

# res = 0
# dfs(1, 1, 0)
# print(res)


def dfs(id, cnt, o) :
    if (id == 12) :
        if (o and cnt == 6) :
            global res
            res += 1
        return
    dfs(id + 1, cnt, o or (id + 1 - cnt > cnt))
    if (cnt < 6) : dfs(id + 1, cnt + 1, o)

res = 0
dfs(1, 1, 0)
print(res)
# (12, 4) + 5(12, 6) + 21(12, 8) + 84(12, 10) + 330(12, 12)