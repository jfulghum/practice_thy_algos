def smallestDifference(x,y):
	x.sort()
	y.sort()
	i1 = 0
	i2 = 0 
	current = float("inf")
	smallest = float("inf")
	while i1 < len(x) and i2 < len(y):
		num1 = x[i1]
		num2 = y[i2]
		if num1 == num2:
	 		 return [num1, num2]
		elif num1 < num2: 
			i1 += 1
			current = num2 - num1
		else:
			i2 +=1
			current = num1 - num2
		if current < smallest:
	  		smallest = current
	  		smallestPair = [num1, num2]
  	return smallestPair 
