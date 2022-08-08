import re
txt="use of python in machine learning "
x=re.search("^use.*learning$ ", txt)
if (x):
   print("yay")
else:
   print("no match")


#print a list of all matches ("in") from a text

t="use of python in machine learning"
x=re.findall("in",t)
print(x)

an="python is one of the most popular languages"
sc= re.search(" \s ", an)
print(sc)