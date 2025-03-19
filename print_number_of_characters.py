#ask user to input their full name 
user_string = input("input your full name = ")

#strip the user string of whitespaces, store in a variables
stripped_string = user_string.strip()

#initialize count
count = 0 

print(stripped_string)
#use for loop to iterate through string characters
for i in stripped_string:
    
    #add 1 to count for each iteration
    count += 1

#return value of count
print(count)