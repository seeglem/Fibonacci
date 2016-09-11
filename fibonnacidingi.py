#hashtag
#created by Hunter Seglem, Jon Staggs, with Counselling from Caleb Barnwell, this is Hunter & Jon's first day of coding.

import math

def fibPrint(n):
	a=0
	b=1
	for i in range(n-1):
		c=a
		a=b
		b=b+c
		print(a)

kCzech=input("Just put a number here and see what happens ")
number=int(kCzech)

fibPrint(number)
