import polarity as p
from hazm import *
import matplotlib
import matplotlib.pyplot as plt
#base part
before_p = []
after_p = []
before_pt = []
after_pt = []
befores = 0
afters = 0
beforest = 0
afterst = 0
file = open('polarityWords.txt')
for i in range(15):
    line = file.readline()
    words = word_tokenize(line)
    print(words)
    print('before')
    before_p.append( p.polarity(words[1],words[0],words[2],'rohaniBeforeCommentsCleaned.txt' ,2000))
    print('after')
    after_p.append(p.polarity(words[1],words[0],words[2],'rohaniAfterCommentsCleaned.txt',2000))
for i in range(15):
    befores += before_p[i]
for i in range(15):
    afters += after_p[i]
print('before p ')
print(befores/15)
print('after p')
print(afters/15)
fig, ax = plt.subplots()
fig1, ax1 = plt.subplots()
ax.plot(before_p,'-o', ms=20, lw=2, alpha=0.7, mfc='orange')
ax1.plot(after_p,'-o', ms=20, lw=2, alpha=0.7, mfc='orange')
plt.show()
true_pos = 0
true_neg = 0
false_pos = 0
false_neg = 0
file1 = open('polarityWords.txt')
file2 = open('posetiveModel.txt')
file3 = open('negativeModel')
for i in range(23):
    f = file1.readline()
    word = word_tokenize(f)
    for j in range(16):
        ff = file2.readline()
        pol = p.polarity1(words[1],words[0],words[2],ff)
        if pol > 0:
            true_pos += 1
        else:
            false_neg += 1
    for j in range(16):
        ff = file3.readline()
        pol1 = p.polarity1(words[1], words[0], words[2], ff)
        if pol1 >= 0:
            false_pos += 1
        else:
            true_neg += 1
print('true pos',true_pos,'true neg',true_neg,'false pos',false_pos,'false neg',false_neg)



