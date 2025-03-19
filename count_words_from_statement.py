#ask user to input a statement with length of desired amount, store in a variable
user_string = input("input a statement (length of desired amount) = ")

#split the user string into a list, store in a variable 
string_list = user_string.split()

#utilize count() to return number of words in user string
print(len(string_list))