#!/usr/bin/env python
import collections
import pickle
import xmltodict

with open("joukahainen.xml") as f:
    doc = xmltodict.parse(f.read())

wordDataMap = collections.OrderedDict()

for wordInf in doc['wordlist']['word']:
    # no infclection or word class information
    if not ('classes' in wordInf.keys() and 'inflection' in wordInf.keys()):
        continue
    # no inflection information
    if not ('infclass' in wordInf['inflection']):
        continue

    # single inflection class
    if type(wordInf['inflection']['infclass']) is str:
        infclass = wordInf['inflection']['infclass']
    # multiple inflection classes, take the first one
    elif type(wordInf['inflection']['infclass']) is list:
        infclass = wordInf['inflection']['infclass'][0]
    # no inflection classes...
    else:
        continue
    # is the word a verb or not (verbs have different infclasses)
    isVerb = wordInf['classes']['wclass'] == 'verb'

    if type(wordInf['forms']['form']) is str:
        word = wordInf['forms']['form']
        if not (word in wordDataMap):
            wordDataMap[word] = (isVerb, infclass)
    elif type(wordInf['forms']['form']) is list:
        # save the information for all words
        for word in wordInf['forms']['form']:
            # if the word already exists, do not rewrite the results
            # ie. keep the first form
            if word in wordDataMap:
                continue
        wordDataMap[word] = (isVerb, infclass)
    else:
        print("something went wrong: ", end = " ")

# save results to a file
pickle.dump(wordDataMap, open("wordInf.pkl", "wb"))

