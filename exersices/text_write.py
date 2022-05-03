file = open("text.txt", 'w')
#Write mode- Over Writes
L = ["This is Delhi \n","This is Paris \n","This is London \n"] 
file.writelines(L)

#reading the above
file = open("text.txt", "r")
print(file.readlines())
print()

#Append
file = open("text.txt", 'a')
file.write("Today \n")
#reading the above
file = open("text.txt", "r")
print(file.readlines())
print()
file.close()

