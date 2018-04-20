
# coding: utf-8

# In[27]:


import string
def main(filename="i_have_a_dream.txt") :
    filename="i_have_a_dream.txt"
    txtfile = open(filename)
    text = txtfile.read()
    from collections import Counter
    unprocess_file=list(text.replace("\n", " ").split(" "))
    list_file = []
    translaotr = str.maketrans('', '', string.punctuation)
    for word in unprocess_file:
        word = word.translate(translaotr)
        if (word != "") :
            list_file.append(word)
    counter = Counter(list_file)
    counter = Counter()
    counter.update(list_file)
    counter.most_common()
    import csv
    with open('count.csv', 'w', newline='') as fin:
        writer = csv.writer(fin, delimiter=',')
        writer.writerow(['word']+['count'])
        for idx, val in counter.most_common():
            writer.writerow([idx, val])
            
    import json
    f = open("count.json", 'w')
    json.dump(counter.most_common(), f)
    json.dump(counter.most_common(), open("count.json", 'w'))
            
    import pickle
    with open('count.pickle', 'wb') as fil:
        pickle.dump(counter.most_common(), fil)
            
if __name__ == '__main__':
    main("i_have_a_dream.txt")

