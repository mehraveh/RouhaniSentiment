from __future__ import unicode_literals
from hazm import *
def hazm1(file_name):
    ff = []
    ff1 = []
    file = open(file_name.__str__(), encoding="utf8")
    normalizer = Normalizer()
    tagger = POSTagger(model='postagger.model')
    file1 = open('polarityADJ.txt')
    file2 = open('polarityTotal.txt' , 'w')
    for i in range(15):
        ff.append(file1.readline())
    for i in range(15):
        ff1.append(word_tokenize(ff[i]))
    for i in range(2000):
        f = file.readline()
        n = normalizer.normalize(f.__str__())
        part_o_speech = tagger.tag(word_tokenize(n))
        print(part_o_speech)
        if len(part_o_speech) > 0 :
            for j in range(len(part_o_speech)):
                if(part_o_speech[j][1] == 'N'):
                    for k in range(15):
                        file2.writelines(part_o_speech[j][0] +' '+ ff1[k][0] +' '+ ff1[k][1] + '\n')


def hazm2(file_name):
    file = open(file_name.__str__(), encoding="utf8")
    normalizer = Normalizer()
    chunker = Chunker(model='chunker.model')
    tagger = POSTagger(model='postagger.model')
    for i in range(2000):
        f = file.readline()
        n = normalizer.normalize(f.__str__())
        tagged = tagger.tag(word_tokenize(n))

        phrases = tree2brackets(chunker.parse(tagged))
def polarity(pos_word, neg_word, phrase, file_name, n):
    near_count_p = 0
    near_count_n = 0
    ind_count_n = 0
    ind_count_p = 0
    ind_count_phrase = 0
    file = open(file_name.__str__(), encoding="utf8")
    print(pos_word)
    for i in range(n):
        comment = file.readline()
        words = word_tokenize(comment.__str__())
        if pos_word in words:
            ind_count_p += 1
        if neg_word in words:
            ind_count_n += 1
        if phrase in words:
            ind_count_phrase += 1
        if pos_word in words and phrase in words:
            near_count_p += 1
        if neg_word in words and phrase in words:
            near_count_n += 1
    print('near posetive')
    print(near_count_p)
    print('near negative')
    print(near_count_n)
    print('ind pos')
    print(ind_count_p)
    print('ind neg')
    print(ind_count_n)
    print('ind phrase')
    print(ind_count_phrase)
    pol = (near_count_p/(ind_count_p * ind_count_phrase + 1)) - (near_count_n/(ind_count_n*ind_count_phrase +1))
    print('polarithy is')
    print(pol*1000)
    return pol*1000

def polarity1(pos_word, neg_word, phrase, comment):
    near_count_p = 0
    near_count_n = 0
    ind_count_n = 0
    ind_count_p = 0
    ind_count_phrase = 0
    words = word_tokenize(comment.__str__())
    if pos_word in words:
        ind_count_p += 1
    if neg_word in words:
        ind_count_n += 1
    if phrase in words:
        ind_count_phrase += 1
    if pos_word in words and phrase in words:
        near_count_p += 1
    if neg_word in words and phrase in words:
        near_count_n += 1
    print('near posetive')
    print(near_count_p)
    print('near negative')
    print(near_count_n)
    print('ind pos')
    print(ind_count_p)
    print('ind neg')
    print(ind_count_n)
    print('ind phrase')
    print(ind_count_phrase)
    pol = (near_count_p/(ind_count_p * ind_count_phrase + 1)) - (near_count_n/(ind_count_n*ind_count_phrase +1))
    print('polarithy is')
    print(pol*1000)
    return pol*1000

#hazm1('rohaniBeforeCommentsCleaned.txt')

