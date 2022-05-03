import re
patten = r"(^[189][0-9]{7}$)"
if re.match(patten , input()):
    print("Valid")
else:
    print("Invalid")
#^is for starts with [189],
# [0-9] digits for {7} repetiotions

# $ to end total of [189] + [0-9]{7} which is equals to 8.


def fun(named_arg, *args):
    print(named_arg)
    print(args)
fun(1,2,3,4,5,6)

def function(x,y, food= "spam"):
    print(food)
function(1,2)
function(3,4, "eggs")
