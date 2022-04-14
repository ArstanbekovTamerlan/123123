arraychik = open('input1.txt', 'r')
file = open('output2.txt', 'w+')
answerik = 0
def f1() :
    for i in stroka :
        for p in stroka :
            if stroka.count(i+p) >= 2 :
               return True
    return False
def f2() :
    for i in range(len(stroka)-2) :
        if stroka[i] == stroka[i+2] :
           return True
    return False
for i in range(1000) :
    stroka = arraychik.readline()
    if (f1() == True and f2() == True) :
        answerik += 1
file.write (str(answerik))
file.close ()