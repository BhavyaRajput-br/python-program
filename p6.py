s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1)
print(s2)
print("union:",s1.union(s2))  #union means s1 m s2 k elemnet add ho jayge 
print("intersection",s1.intersection(s2))
print("difference:" , s1.symmetric_difference(s2))
s3 = s1.union(s2)
print(s3)
print(s1.issubset(s2))
print(s2.issubset(s1))
print(s3.issubset(s2))
