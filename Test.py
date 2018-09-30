li=[[1, 0.23],
	[2, 0.39],
	[4, 0.31],
	[5, 0.27]]

print(li)
li = sorted(li,key= lambda l:l[1])
#[[2, 0.39], [4, 0.31], [5, 0.27], [1, 0.23]]
print(li)


a = [1,2,3]
print(a)
a.append(0)
print(a)