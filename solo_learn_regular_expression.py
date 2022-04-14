import re 

pattern = r"spam"
if re.match(pattern, "spamspamsapm"):
    print("Match")
else:
    print("No match")