Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Answers for a & b:
>>> alkaline_earth_metals = [[4, 9.012], [12, 24.305],[20, 40.078], [38, 87.62],[56, 137.327], [88, 226]]
>>> for metal in alkaline_earth_metals:
	print(metal[0])
	print(metal[1])

	
4
9.012
12
24.305
20
40.078
38
87.62
56
137.327
88
226
>>> 
=============================== RESTART: Shell ===============================
>>> # Answer for c:
>>> alkaline_earth_metals = [[4, 9.012], [12, 24.305],[20, 40.078], [38, 87.62],[56, 137.327], [88, 226]]
>>> number_and_weight=[]
>>> for inner_list in alkaline_earth_metals:
	for items in inner_list:
		number_and_weight.append(items)

		
>>> print(number_and_weight)
[4, 9.012, 12, 24.305, 20, 40.078, 38, 87.62, 56, 137.327, 88, 226]
>>> # Or for another approach:
>>> number_and_weight=[]
>>> for inner_list in alkaline_earth_metals:
	number_and_weight.append(inner_list[0])
	number_and_weight.append(inner_list[1])

	
>>> print(number_and_weight)
[4, 9.012, 12, 24.305, 20, 40.078, 38, 87.62, 56, 137.327, 88, 226]
>>> 
=============================== RESTART: Shell ===============================
>>> # Answer for d:
>>> 
