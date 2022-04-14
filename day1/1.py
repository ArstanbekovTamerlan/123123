arraychik = open('input1.txt', 'r'). read()
file = open('output1.txt', 'w+')
file.write(str(arraychik.count('(')-arraychik.count(')')))
file.close()