arraychik = open('input1.txt', 'r'). read()
file = open('output1.txt', 'w+')
x = 0
y = 0
massiv = []
for i in arraychik :
    f = [x,y]
    if (i == '^') :
        y += 1
    if (i == '>') :
        x += 1
    if (i == 'v') :
        y -= 1
    if (i == '<') :
        x -= 1
    massiv.append(f)
massiv0 = []
for g in massiv :
    if g not in massiv0 :
        massiv0.append(g)
file.write (str(len(massiv0)))
file.close ()
