# n = 1
# while True :
#     d = 5 * n ** 2 + 14 * n + 1
#     if int(d ** 0.5 + 0.5) ** 2 == d :
#         print(n)
#     n += 1

import queue
q = queue.Queue()
q.put((2, -7))
q.put((2, 7))
q.put((0, -1))
q.put((0, 1))
q.put((-4, -5))
q.put((-4, 5))
q.put((-3, -2))
q.put((-3, 2))
