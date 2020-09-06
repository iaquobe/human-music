#!/usr/bin/python3

from essential_generators import DocumentGenerator
gen = DocumentGenerator()
word = gen.gen_word()
print("%s - Human Music" % word)
# print(r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun"))
