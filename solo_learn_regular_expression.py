import re 

pattern = r"spam"
if re.match(pattern, "spamspamspam"):
    print("Match")
elif re.search(pattern, "spamspamspam"):
    print("Found it!")
elif re.findall(pattern, "spamspamsapm"):
    print("found all")
    print(re.findall(pattern, "spamspamspam"))
else:
    print("No match")
