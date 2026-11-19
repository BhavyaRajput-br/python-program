# to print squares of number iiin list....
l1 = [1, 2, 3 ,4 , 5,6 ,7 , 8, 9]
l2= [i*i for i in l1]
print(l2)
l3 = [12,23,32,43,54,65,768,78,87,32,23,23,23,23,23,23]
l4 = [i for i in l3 if i%5==0]
print(l4)
name = ["yash", "raj", "om"]
newname =  [i.upper() for i in name]
print(newname)
name = "yuvraj"
l2 = [i for i in name]
print(l2)