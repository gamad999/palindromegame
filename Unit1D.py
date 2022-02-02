# Convert numbers into palindromes applying the reverse and add rule
print("Program to convert a number into a palindrome")
print("")
number = int(input("Enter a number: "))

conversion = False
numberStr = str(number)

while conversion == False:

	if number != int(numberStr[::-1]):
		number = number + int(numberStr[::-1])
		numberStr = str(number)

	elif number == int(numberStr[::-1]):
		print("")
		print("Conversion to palindrome succesful. The palindrome number is: ", number)
		conversion = True

