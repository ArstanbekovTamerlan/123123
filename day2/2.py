arraychik = open('input1.txt', 'r')
file = open('output2.txt', 'w+')
answerik = 0
def func():
    l,w,h = (int(x) for x in line.split('x'))
    array = [l, w, h]
    titeva = l*w*h
    array.remove(max(array))
    netiteva = (array[0]+array[1])*2
    answer = titeva+netiteva
    return answer
for x in range(1000):
    line = arraychik.readline()
    answerik += int(func())
    if not line:
      break
file.write(str(answerik))
file.close()