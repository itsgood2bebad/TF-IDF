import csv
import pandas as pd

def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count/float(bowCount)
    return tfDict


def computeIDF(docList):
    import math
    idfDict = {}
    N = len(docList)
    
    idfDict = dict.fromkeys(docList[0].keys(), 0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] += 1
    
    for word, val in idfDict.items():
        idfDict[word] = math.log10(N / float(val))
    return idfDict

def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val*idfs[word]
    return tfidf

with open("aroma.csv") as file:  
    reader = csv.reader(file)
    lstA= list(reader)[0]
with open("boulogne_mer.csv") as file:  
    reader = csv.reader(file)
    lstB= list(reader)[0]
with open("comptoir.csv") as file:  
    reader = csv.reader(file)
    lstC= list(reader)[0]
with open("florenpina.csv") as file:  
    reader = csv.reader(file)
    lstD= list(reader)[0]
with open("herbeo.csv") as file:  
    reader = csv.reader(file)
    lstE= list(reader)[0]
with open("nord_plante.csv") as file:  
    reader = csv.reader(file)
    lstF= list(reader)[0]
with open("ruedesplantes.csv") as file:  
    reader = csv.reader(file)
    lstG= list(reader)[0]
    

LA=lstA[0].split(';')
LB=lstB[0].split(';')
LC=lstC[0].split(';')
LD=lstD[0].split(';')
LE=lstE[0].split(';')
LF=lstF[0].split(';')
LG=lstG[0].split(';')

wordSet = set(LA).union(set(LB)).union(set(LC)).union(set(LD)).union(set(LC)).union(set(LD)).union(set(LE).union(set(LF)).union(set(LG)))


wordDictA = dict.fromkeys(wordSet, 0) 
wordDictB = dict.fromkeys(wordSet, 0) 
wordDictC = dict.fromkeys(wordSet, 0) 
wordDictD = dict.fromkeys(wordSet, 0) 
wordDictE = dict.fromkeys(wordSet, 0) 
wordDictF = dict.fromkeys(wordSet, 0) 
wordDictG = dict.fromkeys(wordSet, 0) 



for word in LA:
    wordDictA[word]+=1
    
for word in LB:
    wordDictB[word]+=1

for word in LC:
    wordDictC[word]+=1
    
for word in LD:
    wordDictD[word]+=1

for word in LE:
    wordDictE[word]+=1
    
for word in LF:
    wordDictF[word]+=1
for word in LG:
    wordDictG[word]+=1

df=pd.DataFrame([wordDictA, wordDictB, wordDictC, wordDictD, wordDictE, wordDictF, wordDictG])

tfBowA = computeTF(wordDictA, LA)
tfBowB = computeTF(wordDictB, LB)
tfBowC = computeTF(wordDictC, LC)
tfBowD = computeTF(wordDictD, LD)
tfBowE = computeTF(wordDictE, LE)
tfBowF = computeTF(wordDictF, LF)
tfBowG = computeTF(wordDictG, LG)
idfs = computeIDF([wordDictA, wordDictB, wordDictC, wordDictD, wordDictE, wordDictF, wordDictG])

tfidfBowA = computeTFIDF(tfBowA, idfs)
tfidfBowB = computeTFIDF(tfBowB, idfs)
tfidfBowC = computeTFIDF(tfBowC, idfs)
tfidfBowD = computeTFIDF(tfBowD, idfs)
tfidfBowE = computeTFIDF(tfBowE, idfs)
tfidfBowF = computeTFIDF(tfBowF, idfs)
tfidfBowG = computeTFIDF(tfBowG, idfs)


