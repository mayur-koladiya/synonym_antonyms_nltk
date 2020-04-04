import nltk 
from nltk.corpus import wordnet 


  
w1 = wordnet.synset('eat.v.01') # v here denotes the tag verb 
w2 = wordnet.synset('consume.v.01') 
print("verb : ",w1.wup_similarity(w2)) 


w1 = wordnet.synset('door.n.01') 
w2 = wordnet.synset('gate.n.01') # n denotes noun 
print("noun : ",w1.wup_similarity(w2)) 