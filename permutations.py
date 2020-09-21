from itertools import permutations
from nltk.corpus import words

list_of_letters = []
number_of_letters = int(input('How many letters are in total: '))

for i in range(0, number_of_letters):
    list_of_letters.append(input('Write char' + str(i+1) + str(": ")))

no_of_perm = int(input('Write length of permutations: '))
perm = permutations(list_of_letters, no_of_perm)

new_list = []
for i in list(perm):
    new_list.append("".join(i))

print('Possible words are listed below: \n')
print('===================================')
for i in range(len(new_list)):
    if(new_list[i] in words.words()):
        print(new_list[i])
print('===================================')
