arraychik = open('input1.txt','r'). read()
file = open('output2.txt','w+')
kykycik = 0
f = 0
for tixacik in arraychik :
    f += 1
    if (tixacik == '('):
        kykycik += 1
    if (tixacik == ')'):
        kykycik -= 1
    if (kykycik == -1):
       break
file.write(str(f))
file.close()
