#import nltk
  
# Importing jaccard distance and ngrams from nltk.util
from nltk.metrics.distance import jaccard_distance  # Used to measure the dissimilarity between two words
from nltk.util import ngrams

from nltk.corpus import words
correct_words = words.words()
user_input = input("Enter a sentence : ")

# rinting original string
print ("The original sentence is : " +  user_input)
 
# using split() to extract each individual word from the user innput
res = user_input.split()
 
# printing result
print ("The list of words is : " +  str(res))  

sent = ""
# Looping the res list to find the correct spellings based on jaccard distance and printing the correct words
for word in res:
    temp = [(jaccard_distance(set(ngrams(word, 2)),
                              set(ngrams(w, 2))),w)
                              for w in correct_words if w[0]==word[0]]
    print(sorted(temp, key = lambda val:val[0])[0][1])


