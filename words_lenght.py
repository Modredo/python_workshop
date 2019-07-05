''' after you pip install nltk for the first time you still
    have to download the words list. Do this by running:
    
    import nltk 
    nltk.download()

    select download and on the list search for words
'''   
from nltk.corpus import words

n_char    = 6  #max word lenght to check
c         = 0 

print('getting the words list and sorting by lenght.')
# get a list of words
word_list = words.words()
#print(len(word_list))
#sort the list by lenght 
words_lsort = sorted(word_list,key = len) 

print('....')
print(f'counting words shorter than {n_char} characters') 

for word in words_lsort:
    if len(word) <= n_char:
        c = c + 1

print('Checking Completed.')
print(c)
