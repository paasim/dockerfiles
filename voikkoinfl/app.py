#!/usr/bin/env python

import sys
import voikko.voikkoinfl as infl

noun_types = infl.readInflectionTypes('subst.aff')

if len(sys.argv) == 3:
    inflected = infl.inflectWord(sys.argv[1], sys.argv[2], noun_types)

    for w in inflected:
        print(w.formName + ': ' + w.inflectedWord)
else:
    print('Usage: [app] word infl-class, e.g.')
    print('         app talo valo            ')

