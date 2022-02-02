# Create a function that allows the students to calculate the sum of the digits of a number

print("Function for calculating the sum of the digits of a number")
print("")
number = int(input("Please enter number: "))

def digitsSum(num):

	sumDig = 0

	while num != 0:
		sumDig = sumDig + num % 10
		num = num//10

	return sumDig

print("The sum of the number's digits is: ", digitsSum(number))
