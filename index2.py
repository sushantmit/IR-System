from collections import OrderedDict

doclist = ["doc3", "doc4", "doc5"]
text = {}
index = []
for file in doclist:
	fhandle = open(file,"r")
	str1 = fhandle.read().lower()
	if str1[len(str1)-1] == '.':
		str1 = str1[:len(str1)-1]
	str1 = str1.replace(". "," ")
	lst = str1.split()
	text[file] = lst
	for terms in lst:
		index.append(terms)

index = sorted(list(set(index)))
postings = OrderedDict((word, [0,[]]) for word in index)
for term in index:
	for doc in text:
		if term in text[doc]:
			postings[term][1].append(doc)
			postings[term][0] = postings[term][0] + 1

#index is a list of terms sorted in alphabetical order
#postings is the inverted index that consists of posting lists sorted in alphabetical order



def intersect(p1, p2):
	answer = []
	for doc in p1:
		for doc1 in p2:
			if doc1 == doc:
				answer.append(doc)
				p2.remove(doc)
				break
	return answer

fanswer = []

def multintersect(qlst):
	fanswer = qlst[0][1]
	qlst = qlst[1:]
	while (len(qlst) != 0 and len(fanswer) != 0):
		fanswer = intersect(fanswer, qlst[0][1])
		qlst = qlst[1:]
	if(len(fanswer) > 0):
		return fanswer
	else:
		return 0

def hello(query):
	# query = raw_input("Input your query(can use AND operator): ")
	query = query.split(" AND ")
	answer = [0,[]]
	qlists = []

	for term in query:
		if term.lower() in postings:
			qlists.append(postings[term.lower()])
		else:
			exit()

	for i in range(len(qlists)-1):
		for j in range(len(qlists)-1):
			if qlists[j][0]>qlists[j+1][0]:
				temp = qlists[j]
				qlists[j] = qlists[j+1]
				qlists[j+1] = temp

	return multintersect(qlists)