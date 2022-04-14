import re
pattern = r"pam"
#using other regex functions
match= re.search(pattern, "eggspamsausage")
if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())
#using sub functions which does substitution
str = "My name is meron. Hi meron."
pattern = r"meron"
newstr = re.sub(pattern, "astu", str)
print(newstr)
pattern = r"^gre.y$"
if re.match(pattern, "grep"):
    print("matcg 1")
#using group
pattern = r"a(bc)(de)(f(g)h)i"
kl = re.match(pattern, "abcdefghijklmnop")
if kl:
    print(kl.group())
    print(kl.group(0))
    print(kl.group(2))
    print(kl.group(3))
    print(kl.groups())
else:
    print("sorry")
