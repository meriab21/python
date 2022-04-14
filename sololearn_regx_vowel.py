import re
words = str(input())
pattern = r"[aeiou]"
if re.search(pattern, words):
    print("has vowels")
else: 
    print("has no vowels")
pattern = r"egg(spam)*"