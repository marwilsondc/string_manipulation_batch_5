#initialize capitalized_list
capitalized_list = list()

#ask the user to input their full name in incorrect casing and store it in a variable
user_input = input("enter your full name in incorrect casing = ")

#split the user string into a list, store in a variable
string_list = user_input.split()

#use for-loop to iterate through list
for noun in string_list:

    #convert string casing into lower
    step_one = noun.lower()

    #capitalize string
    step_two = step_one.capitalize()

    #append capitalized nouns to capitalized_list
    capitalized_list.append(step_two)

#use join() to reconvert list into string
capitalized_result = " ".join(capitalized_list)
print(capitalized_result)