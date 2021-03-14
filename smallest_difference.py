def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
	arrayTwo.sort()
	current = float("inf")
	smallest = float("inf")
	i1 = 0 
	i2 = 0
	while i1 < len(arrayOne) and i2 < len(arrayTwo):
		num1 = arrayOne[i1]
		num2 = arrayTwo[i2]
		if num1 == num2:
			return [num1, num2]
		elif num1 < num2:
			current = num2 - num1
			i1 += 1
		else:
			current = num1 - num2
			i2 +=1 
		
		if current < smallest:
			smallest = current
			smallest_difference = [num1, num2]
	return smallest_difference


				
