from collections import Counter
sentence = "python is easy and python is powerful"

words = sentence.split()
freq = Counter(words)

for w, c in freq.items():
    print(w, ":", c)


#Ans Count each word frequency : python : 2
# is : 2
# easy : 1
# and : 1
# powerful : 1

#-------------------------------


from collections import Counter

sentence = "python is easy and python is powerfull"

print(dict(Counter(sentence.split())))



#Ans: Store in Dictionary = {'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerfull': 1}
