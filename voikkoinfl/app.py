#!/usr/bin/env python

import sys
import pickle
import voikko.voikkoinfl as infl

noun_types = infl.readInflectionTypes('subst.aff')
verb_types = infl.readInflectionTypes('verb.aff')
infclass_map = pickle.load(open('wordInf.pkl', 'rb'))

if len(sys.argv) == 2:
    word = sys.argv[1]
    if word in infclass_map:
        word_infclass = infclass_map[word]
        if word_infclass[0]:
            types = verb_types
        else:
            types = noun_types

        inflected = infl.inflectWord(word, word_infclass[1], types)

        for w in inflected:
            print(w.formName + ': ' + w.inflectedWord)
    else:
        print('Inflection data not found found, either a typo or a problem with the inflection dataset.')
else:
    print('Usage: [app] word, e.g.')
    print('         app talo      ')
