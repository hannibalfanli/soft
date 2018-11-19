import string
def head():
	catalog=['sid','name','age','classid']
	print("|{:<10}|{:<10}|{:<10}|{:<10}".format(catalog[0],catalog[1],catalog[2],catalog[3]))
	print('------------------------------------------')

def searchstu(studentadd):
	print('============== 学员信息浏览 ==============')
	head()
	'''
	catalog=['sid','name','age','classid']
	print("|{:<10}|{:<10}|{:<10}|{:<10}".format(catalog[0],catalog[1],catalog[2],catalog[3]))
	print('------------------------------------------')
	'''
	#stu=['1','zhangsan','20','python01']
	for i in range(len(studentadd)):
		print("|{:<10}|{:<10}|{:<10}|{:<10}".format(i+1,studentadd[i][0],studentadd[i][1],studentadd[i][2]))
	button1=input("请按回车键继续:")
	while button1 !='':
		button1=input("请按回车键继续:")

def addstu(studentadd):
	print('==============  添加学员信息 ==============')
	student=[]
	student.append(input("请输入学员的姓名:"))
	student.append(input("请输入学员的年龄:"))
	student.append(input("请输入学员的班级号:"))
	studentadd.append(student)
	button2=input("学员信息添加成功！按回车键继续:")
	while button2 !='':
		button2=input("请按回车键继续:")
	return studentadd

def delstu(studentadd):
	print('============== 删除学员信息 ==============')
	head()
	#catalog=['sid','name','age','classid']
	#print("|{:<10}|{:<10}|{:<10}|{:<10}".format(catalog[0],catalog[1],catalog[2],catalog[3]))
	#print('------------------------------------------')
	#stu=['1','zhangsan','20','python01']
	for i in range(len(studentadd)):
		print("|{:<10}|{:<10}|{:<10}|{:<10}".format(i+1,studentadd[i][0],studentadd[i][1],studentadd[i][2]))
	
	a=input('请输入要删除的学员信息的序号sid(0为放弃本次删除):')
	
	#判断回车和字符串输入
	while a == '' or a.isdigit() == False:
		a=input('请输入正整数序列号:')
	
	a=int(a)
	#print('a=',a)
	
	if a == 0:
		return studentadd
	
	while a > len(studentadd):
		if len(studentadd)==0:
			print("当前没有可删除学员信息，请添加")
			return studentadd
		print("未找到该序号为:%d的学员信息"%a)
		a=int(input('请正确输入要删除的学员信息的序号sid:'))
		#print(type(a))
	while a < 0:
		a=int(input('请输入正整数序列号:'))
	#if a < 0:
	#	print('请输入正整数序列号')
	#	return studentadd
	#print('a=',a)
	#print(string.atof(a))
	studentadd.pop(a-1)
	head()
	for i in range(len(studentadd)):
		print("|{:<10}|{:<10}|{:<10}|{:<10}".format(i+1,studentadd[i][0],studentadd[i][1],studentadd[i][2]))
	button3=input('学员信息删除成功！按回车键继续:')
	while button3 !='':
		button3=input("请按回车键继续:")
	return studentadd

def main():
	print("============== 学员管理系统 ==============")
	print(" 1.查看学员信息      2.添加学生信息")
	print(" 3.删除学员信息      4.退出系统")
	print("==========================================")
	a=input("请输入对应的选择:")
	while a.isdigit() == False:
		a=input("选择错误,请输入正确的选择:")
	#int(a)
	#return a不生效
	return int(a)

chose=main()
studentadd=[['zhangsan',20,'python01'],['lisi',22,'python02']]
while True:
	#print('11')
	#print(type(chose))
	if chose==1:
		searchstu(studentadd)
	elif chose ==2:
		studentadd=addstu(studentadd)
	elif chose ==3:
		studentadd=delstu(studentadd)
	elif chose ==4:
		break
	else:
		print('please input the true number!')
	chose=main()
print('Good bye! Thank You!')



