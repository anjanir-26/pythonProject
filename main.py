a= {"Name": "Anjani", "ID" : 2100031319 ,"Branch" : "CSE" }
b=a.copy()
print(b)
a.popitem()
print(a)
print(a.items())
a.clear()
print(a)
b.pop("Name")
print(b)
print(b.get("ID"))
b.update({"Branch":"CSE(H)"})
print(b)
print(b.keys())