# (12017639147 + 1) // 2 == 6008819574
from utils import prime_factorize
n = 6008819574
factors = prime_factorize(n + 1)
unique_factors = list(set(factors))
l = len(unique_factors)
L = 2 ** l 
ans = (n + 1) // 3

def con(x) :
    if x % 3 == 2 : return (n // x + 2) // 3
    if x % 3 == 1 : return (n // x + 1) // 3
    return 0

for st in range(1, L) :
    sta = st
    now = 1
    cnt = 0
    for k in range(l) :
        if sta & 1 :
            now *= unique_factors[k]
            cnt += 1
        sta //= 2
    if cnt & 1 : ans -= con(now)
    else : ans += con(now)
print(ans)
    

# import nltk
# from itertools import  permutations
# nltk.download('words')
# english_words = set(nltk.corpus.words.words())

# a = ['never', 'name', 'koala', 'tunnel', 'toast', 'youth', 'ticket', 'medal', 'road', 'kuwait']
# b = ['income', 'wisdom', 'kidney', 'yummy', 'helix', 'madam', 'kelvin', 'riddle', 'enemy', 'mute', 'kappa', 'haste', 'oxygen', 'remake', 'yard', 'simony', 'wedge', 'humane', 'seat', 'sure']
# f = [False for _ in range(20)]

# def sk(now, res) :
#     if (now == 5) :
#         flag = True
#         s = [res[i][2] for i in range(5)]
#         for i in permutations(s, 5) : 
#             st = 't' + ''.join(i) 
#             if st in english_words :
#                 flag = False
#                 print(st)
#                 break
#         if (flag) : return
#     if (now == 10) :
#         st = res[5][2] + res[6][2] + res[7][2] + res[8][2] + res[9][2] + 'e'
#         if not st in english_words : return
#         print(res)

#     for i in range(20) :
#         if (len(a[now]) != len(b[i]) or f[i]) : continue
#         f[i] = True
#         for j in range(20) :
#             if (f[j]) : continue
#             cnt = 0
#             for k in range(len(a[now])) :
#                 if (a[now][k] == b[i][k] or a[now][k] in b[j] or b[i][k] in b[j]) : continue
#                 if (cnt == 0) : cnt = k
#                 else : 
#                     cnt = 0
#                     break
#             if (cnt) : 
#                 f[j] = True
#                 res[now] = (b[i], b[j], a[now][cnt] + b[i][cnt])
#                 sk(now + 1, res)
#                 f[j] = False
#         f[i] = False

# sk(0, [0 for _ in range(10)])