'''' after you pip install nltk for the first time you still
    have to download the words list. Do this by running:
    
    import nltk 
    nltk.download()

    select download and on the list search for words
'''   
import requests 
from time import sleep
from nltk.corpus import words
from random import randint

n_char    = 6  #max word lenght to check
checked   = 0
available = 0
taken     = 0
ava_list  = []
url       = 'https://github.com/'

print('getting the words list and sorting by lenght.')
# get a list of words
word_list = words.words()
#print(len(word_list))
#sort the list by lenght 
words_lsort = sorted(word_list,key = len) 

print('....')
print(f'Checking availability for words shorter than {n_char} characters')

for word in words_lsort:
    if len(word) <= n_char:
        check_url = url + word


        if requests.get(check_url).status_code == 200:
            ava_list.append(word)
            available = available+ 1
        else:
            taken = taken + 1
        checked = checked + 1
    sleep(randint(1,3))

print('Checking Completed.')
print(f'    checked:   {checked}')
print(f'    available: {available}')
print(f'    taken:     {taken}') 
print('Writing list to file...') 

with open('available_gits.txt','w') as f:
    f.write(str(ava_list))

print('Write to file completed')

