n = int(input("Input and integer less than 256 : "))
n_original = n
d = 128
binString ="" 
for i in range(0,8):
	q = int(n / d)
	r = int(n % d)
	print(d,q,r)
	n = r
	d = int(d / 2)
	binString = binString+str(q)
print("\n*********\t")
print
print(str(n_original)+" base 10 = " +binString+ " base 2")
print("\n*********\t")
