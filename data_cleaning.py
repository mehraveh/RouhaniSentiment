"""delete numbers and english words"""
file = open('rohaniBeforeCommentsTest.txt', encoding="utf8")
file1 = open('rohaniBeforeCommentsTestCleaned.txt', 'w' , encoding='utf8')
for i in range(1000):
    c = file.readline()
    print ('last c')
    print (c)
    for j in c:
        if ord(j)<=127 and ord(j)>0 and ord(j) != 32 :
            print (j)
            c = c.replace(j, "")
        if ord(j) > 100000:
             c = c.replace(j, '')
    print ('next c')
    print (c.__str__())
    file1.writelines(c.__str__() + '\n')

