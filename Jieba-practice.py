import jieba
import os

jieba.load_userdict('./Resource/MyDict.txt')
stopWords = list()
with open('./Resource/StopWord.txt', 'r', encoding='utf-8') as f:
    stopWords = [w.replace('\n', '') for w in f.readline()]
    
sb = ''
for fileName in os.listdir('./res_gossiping'):
    filePath = './res_gossiping/' + fileName

    with open(filePath, 'r', encoding='utf-8') as f:
        sb += f.read().split('---split---')[0]
        
wordCut = jieba.cut(sb)
wordCutList = [w for w in wordCut]

wordCountDict = dict()
for w in wordCutList:
    if (w.__len__() < 2) or (w in stopWords):
        continue
    if w in wordCountDict:
        wordCountDict[w] += 1
    else:
        wordCountDict[w] = 1

wordCountDict
wordCutList = [(k, v) for k, v in wordCountDict.items()]
wordCutList.sort(key=lambda x: x[1], reverse=True)
pritt(wordCutList)
