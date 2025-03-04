import os
rt = 'D:\\fangxk2003\\projectEuler\\P151~200'
os.chdir(rt)
files = os.listdir()
for file in files:
    p = os.path.join(rt, file, 'sol.py')
    os.rename(p, os.path.join('D:\\fangxk2003\\projectEuler', '1', 'p1' + file[-2:] + '.py'))