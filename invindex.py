from collections import OrderedDict
import os

doclist = os.listdir("Documents")                   #List of Document File Names Obtained
text = {}
index = []
for file in doclist:                                #Tokenising and storing terms
    fhandle = open('Documents/'+file,"r")
    str1 = fhandle.read().lower()
    if str1[len(str1)-1] == '.':
        str1 = str1[:len(str1)-1]
    str1 = str1.replace(". "," ")
    str1 = str1.replace(", "," ")
    lst = str1.split()
    text[file] = lst
    for terms in lst:
        index.append(terms)
                                                    #Creation of Inverted Index as a Dictionary data type
index = sorted(list(set(index)))
postings = OrderedDict((word, [0,[]]) for word in index)
for term in index:
    for doc in text:
        if term in text[doc]:
            postings[term][1].append(doc)
            postings[term][0] = postings[term][0] + 1
for term in postings:
    print term, " : ", postings[term][0], " : ", postings[term][1]

#Index is a list of terms sorted in alphabetical order
#postings is the inverted index that consists of posting lists sorted in alphabetical order
