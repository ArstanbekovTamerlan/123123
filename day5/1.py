arraychik = open('input1.txt', 'r')
file = open('output1.txt', 'w+')
answerik = 0
def f1() :
    yslovchik = 'aeiou'
    ans = 0
    for i in range(len(stroka)) :
        if stroka[i] in yslovchik :
            ans += 1
        if ans >= 3 :
            return True
    return False
def f2() :
   for i in range(len(stroka)-1) :
       if stroka[i] == stroka[i+1] :
           return True
   return False
def f3() :
    sigl = ['ab','cd','pq','xy']
    for i in range(len(stroka)-1) :
        if (stroka[i] + stroka[i+1] in sigl) :
            return True
    return False
for i in range(1000) :
    stroka = arraychik.readline()
    if (f1() == True and f2() == True and f3() == False) :
        answerik += 1
file.write (str(answerik))
file.close ()