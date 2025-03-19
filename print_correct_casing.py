#ask the user to input their full name in incorrect casing and store it in a variable
user_input = input("enter your full name in incorrect casing = ")

#split the user string into a list, store in a variable
string_list = user_input.split()

#use for-loop to iterate through list
for noun in string_list:

    #convert string casing into lower
    noun.lower()

    #capitalize string
    noun.capitalize()

#use join() to reconvert list into string
capitalized_result = string_list.join()
print(capitalized_result)