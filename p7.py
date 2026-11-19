dict = {"Name":7, "Roll no ": 39 , "marks": 100}
print(dict)
dict.update({"cont": 1234})
del dict ["marks"]
print(dict)
print(dict.keys())
print(dict.values())
print(dict.items())
for  i in dict.keys():
  print(1)
for i in  dict.items():
   print(i)
for x,y in dict.items():
  print("[", x,":" , y, "]")
  print(dict.get("name"))
dict = dict.copy()
dict.clear()
#nested dictionary
list  = ([12, "Om"], [23, "Jay"])
dict = {1: {"Roll":12, "Name":"Om"}, 2: {"Roll" : 24, "Name " : "Jay"}}
print(dict[1])
print(dict[2]["Roll"])
print(dict[1]["Name"])
#Dictionary comprehension
d1 = {1:"One", 2 : "Two", 3:"Three", 4:"Four"}
d2={i:i for i in range(1,11)}
print(d2)
d3 ={}
d3 = {x:y for x,y in d1.items() if x%2==0}
print(d3)
l1 = ["Roll", "Name", "Marks"]
l2 = [12, "Jayesh", 63.22]
student = {l1[i]:l2[i] for i in range(len(l1))}
print(student)
print(student.keys())
print(student.values())