#!/usr/bin/python3

import re

def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):    
        return re.search(pattern, word)
    def apply_rule(word):    
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)    

patterns = \ 
  (
    ('[sxz]$',           '$',  'es'),
    ('[^aeioudgkprt]h$', '$',  'es'),
    ('(qu|[^aeiou])y$',  'y$', 'ies'),
    ('$',                '$',  's')    
  )

rules = [build_match_and_apply_functions(pattern, search, replace)  
         for (pattern, search, replace) in patterns]

noun = 'boxxxxx'

for matches_rule, apply_rule in rules:  
    if matches_rule(noun):
        print(apply_rule(noun))
        break

