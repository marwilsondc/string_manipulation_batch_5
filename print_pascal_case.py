#ask user to input their full name
user_string = input("input your full name in incorrect casing = ")

#convert casing of user string to lowercase
step_one = user_string.lower()

#convert casing of user string to title string
step_two = step_one.title()

#delete whitespaces with replace()
final_string = step_two.replace(" ", "")

#print user string
print(final_string)