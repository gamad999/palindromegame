# Interact with the user
# Review of the previous lesson and additional activities

print("Workflow for the applying process of the concepts of the thematic unit 1")
print("")
print("Welcome to the Palindrome program")
print("")
welcome = input("Enter your name: ")
print("")
message = input("Enter message: ")
print("")
question = input("Do you know a palindrome? Write it!: ")
print("")
autor = input("Do you know who devised it? mention him/her!: ")
print("")

print("Hello ", welcome, ", welcome to the Palindrome program")

#print(message)

# Reverse the reading direction of a string of characters or text (message)
# Visualization of the string read from left to right and from right to left
print("")
print("Message read from left to right: ", message)
print("")
print("Message read from right to left: ", message[::-1])
print("")
print("Your palindrome read from left to right: ", question, "It was devised by: ", autor)
print("")
print("Your palindrome read from right to left: ", question[::-1])