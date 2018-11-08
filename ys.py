print ('hello word')
'''
i=1
b=1
while i<10:
	print('i=',i)
	print('b=',b)
	i+=2
	b+=2
while i>0:
	print('i-=',i)
	print("b-=",b)
	i-=1
	b-=1
'''
#a=1
for i in range(1,10):
	for j in range(1,i+1):
		print("{}*{}={:<3}".format(j,i,i*j),end=" ")
	print("")
for i in range(9,0,-1):
	for j in range(1,i+1):
		print("{}*{}={:<3}".format(j,i,i*j),end=" ")
	print("")
print("hello word")