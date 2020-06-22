def prime():
	n=int(input("enter the num:"))
	for i in range(2,n):
			if n%2==0:
				print("not prime")
				break
	else:
				print("prime")
prime()				
			