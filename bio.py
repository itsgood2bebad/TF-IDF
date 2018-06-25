from urllib.request import urlopen
import nltk
import bs4 as BeautifulSoup
import re
import unidecode
import csv


def netoyage(file):
    file= re.sub(r"[\d#$€%&<>\"\?\!(),;:/@...\+]","",file)
    file = unidecode.unidecode(file)
    file= file.lower().split()
    return file


html = urlopen('http://www.brin-d-herbe.fr/categories/71-tisanes-brin-d-herbe').read()
soup = BeautifulSoup.BeautifulSoup(html,"lxml")

i=0
file =''
for elem in soup.findAll():
    if "{" in elem.text :
        continue
    file += elem.text
    #print(i,elem.text)
    #i+=1

file = netoyage(file)

nltk_stopwords = nltk.corpus.stopwords.words('french')
lst=[]
for i in file :
    if i not in nltk_stopwords or len(i)> 2:
        lst.append(i)

with open('brin_dherbe.csv', 'w') as myfile:
    wr = csv.writer(myfile,delimiter=';')
    wr.writerow(lst)