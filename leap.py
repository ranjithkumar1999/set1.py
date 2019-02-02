#leap_year or not
#ranjith
x=int(input())
if x==4:
	if x==100:
		if x==400:
			print("leap")
		else:
			print("not")
	else:
		print("leap")
else:
	print("not")
