#ask user to enter their full name in incorrect casing
user_string = input("input your name in incorrect casing = ")

#convert user string to lower case
convert_lower = user_string.lower()

#convert whitespaces to underscore
final_result = convert_lower.replace(" ", "_")

#print result
print(final_result)